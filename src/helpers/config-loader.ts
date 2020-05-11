
import * as fs from 'fs-extra';
import * as path from 'path';
import * as YAML from 'js-yaml';
import deepmerge from 'deepmerge';

import { Enemy, Stat } from '../models';

// this mirrors config.yml
export interface ModConfig {
  version: number;

  seed: number;

  global: Record<Stat, number>;
  boss: Record<Stat, number>;
  monster: Record<Stat, number>;
  shinju: Record<Stat, number>;
  part: Record<Stat, number>;

  specific: Record<string, Record<Stat, number>>;
}

export interface ConfigLoaderOpts {
  overrides: Partial<ModConfig>;
}

export class ConfigLoader {

  public get finalConfig(): ModConfig {
    return this.config;
  }

  private config!: ModConfig;
  
  constructor(private opts: ConfigLoaderOpts) {
    this.init();
  }

  private init(): void {
    try {

      // load config.yml
      const config = YAML.safeLoad(fs.readFileSync(path.join(__dirname, '..', '..', 'config', 'config.yml')).toString());

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
      console.error(`Could not find config.yml in config/. Please place one there.`);
      process.exit(1);
    }
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