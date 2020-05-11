
import * as fs from 'fs-extra';
import * as path from 'path';
import * as YAML from 'js-yaml';
import deepmerge from 'deepmerge';

import { Enemy, Stat } from '../models';

// this mirrors config.yml
export interface ModConfig {
  version: number;

  seed: number;

  installTo: string;

  global: Record<Stat, number>;
  boss: Record<Stat, number>;
  monster: Record<Stat, number>;
  shinju: Record<Stat, number>;
  part: Record<Stat, number>;

  specific: Record<string, Record<Stat, number>>;
}

export interface ConfigLoaderOpts {
  overrides: Partial<ModConfig>;
  configLocation?: string;
}

export class ConfigLoader {

  public get finalConfig(): ModConfig {
    return this.config;
  }

  private config!: ModConfig;
  private validKeys = [
    'version', 'seed', 'installTo',
    'global', 'boss', 'monster', 'shinju', 'part', 'specific'
  ];
  
  constructor(private opts: ConfigLoaderOpts) {
    this.init();
  }

  private init(): void {
    try {

      const configLocation = this.opts.configLocation || path.join(__dirname, '..', '..', 'config', 'config.yml');

      // load config.yml
      const config = YAML.safeLoad(fs.readFileSync(configLocation).toString());

      // if you specify override.global (via cli), copy those values to the other sections
      if(this.opts.overrides) {
        Object.keys(this.opts.overrides.global || {}).forEach(key => {
          ['boss', 'monster', 'shinju', 'part'].forEach(masterKey => {
            (this.opts.overrides as any)[masterKey] = (this.opts.overrides as any)[masterKey] || {};
            (this.opts.overrides as any)[masterKey][key] = (this.opts.overrides as any).global[key];
          });
        });
      }
  
      // merge the two configs into the finalized config
      this.config = deepmerge(config, this.opts.overrides || {});
    } catch(e) {
      console.error(`Could not find config.yml in config/. Please place one there or specify --config.`);
      process.exit(1);
    }

    this.validateConfig();
  }

  // validate the config file
  private validateConfig(): void {
    Object.keys(this.config).forEach(key => {
      if(this.validKeys.includes(key)) return;

      console.error(`Invalid config setting: ${key}. Remove it from your config and try again.`);
      process.exit(1);
    });

    const validateStatBlock = (statBlock: string): void => {
      const validKeys = Object.values(Stat);
      Object.keys(this.config[statBlock as keyof ModConfig]).forEach(statKey => {
        if(validKeys.includes(statKey as Stat)) return;

        console.error(`Invalid config setting: ${statBlock}.${statKey}. Remove it from your config and try again.`);
        process.exit(1);
      });
    };

    ['global', 'boss', 'monster', 'shinju', 'part'].forEach(parent => {
      validateStatBlock(parent);
    });
  }

  public getStats(enemy: Enemy): Record<Stat, number> {

    // get the type of enemy and the specific name overrides if possible
    const type = this.config[enemy.type] || {};
    const specific = this.config.specific[enemy.name] || {};

    const stats: any = {};

    // take the stats in the priority order: specific name, type, ... if none, multiply by 1
    Object.values(Stat).forEach(stat => {
      stats[stat as Stat] = specific[stat] || type[stat] || 1;
    });

    return stats as Record<Stat, number>;
  }

}