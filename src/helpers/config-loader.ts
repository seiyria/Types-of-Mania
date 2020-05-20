
import * as fs from 'fs-extra';
import * as path from 'path';
import * as YAML from 'js-yaml';
import deepmerge from 'deepmerge';

import { Enemy, Stat } from '../models';
import { getDefaultConfig } from './default-config';

export interface ModConfig {
  version: number;

  seed: number|string;

  installTo: string;
  pakName: string;

  base: Record<Stat, number>;
  boss?: Partial<Record<Stat, number>>;
  monster?: Partial<Record<Stat, number>>;
  shinju?: Partial<Record<Stat, number>>;
  part?: Partial<Record<Stat, number>>;

  specific: Record<string, Record<Stat, number>>;
}

export interface ConfigLoaderOpts {
  overrides: Partial<ModConfig>;
  configJson?: string;
  configLocation?: string;
}

export class ConfigLoader {

  public get finalConfig(): ModConfig {
    return this.config;
  }

  private config!: ModConfig;
  private validKeys = [
    'version', 'seed', 'installTo', 'pakName',
    'base', 'boss', 'monster', 'shinju', 'part', 'specific'
  ];
  
  constructor(private opts: ConfigLoaderOpts) {
    this.init();
  }

  private init(): void {

    const configLocation = this.opts.configLocation || 'config/config.yml';

    let config: ModConfig;

    // load the configJson first, or try to
    // it should be a full config object, ideally, not a partial
    if(this.opts.configJson) {
      try {
        config = deepmerge(getDefaultConfig(), JSON.parse(this.opts.configJson));
      } catch(e) {
        console.log('Could not load --configJson correctly. Cancelling...');
        process.exit(0);
      }
    
    // if there is no configJson passed in, try to load config.yml
    } else {
      try {
        config = YAML.safeLoad(fs.readFileSync(path.resolve(configLocation)).toString());

      } catch(e) {
        console.log(`Could not find config.yml at ${configLocation}. Please place one there or specify --config.`);
        process.exit(0);
      }
    }

    // if you specify override.base (via cli), copy those values to the current config
    config = deepmerge(config!, this.opts.overrides || {});

    // apply the base to all other aspects
    (Object.keys(config!.base || {}) as Array<Stat>).forEach(baseStatKey => {
      (['boss', 'monster', 'shinju', 'part'] as Array<'boss'|'monster'|'shinju'|'part'>).forEach(masterKey => {   
        config[masterKey] = config[masterKey] || {};
        
        if(config[masterKey]![baseStatKey]) return;

        config[masterKey]![baseStatKey] = config.base[baseStatKey];
      });
    });

    // set the finalized config
    this.config = config! as ModConfig;

    this.validateConfig();
  }

  // validate the config file
  private validateConfig(): void {

    // validate top level keys
    Object.keys(this.config).forEach(key => {
      if(this.validKeys.includes(key)) return;

      console.log(`Invalid config setting: ${key}. Remove it from your config and try again.`);
      process.exit(0);
    });

    // validate stat blocks
    const validateStatBlock = (statBlock: Record<Stat, number>): void => {
      const validKeys = Object.values(Stat);

      Object.keys(statBlock).forEach(statKey => {
        if(validKeys.includes(statKey as Stat)) return;

        console.log(`Invalid config setting: ${statKey}. Remove it from your config and try again.`);
        process.exit(0);
      });
    };

    // validate top level stat blocks
    ['base', 'boss', 'monster', 'shinju', 'part'].forEach(parentKey => {
      validateStatBlock(this.config[parentKey as 'base'|'boss'|'monster'|'shinju'|'part'] as Record<Stat, number>);
    });
    
    // validate specific stat blocks
    Object.keys(this.config.specific || {}).forEach(specificStatBlock => {
      validateStatBlock(this.config.specific[specificStatBlock]);
    });
  }

  public getStatMultipliers(enemy: Enemy): Record<Stat, number> {

    // get the type of enemy and the specific name overrides if possible
    const type = this.config[enemy.type] || {};

    const stats: any = {};

    // take the stats in the priority order: type, ... if none, multiply by 1
    Object.values(Stat).forEach(stat => {
      stats[stat as Stat] = type[stat] || 1;

      // then we check each specific key against the enemy name to see if we should apply anything further
      Object.keys(this.config.specific || {}).forEach(specificKey => {

        // we do a case insensitive match on the regex first
        const checkRegex = new RegExp(specificKey, 'i');
        if(!enemy.name.match(checkRegex) && !enemy.id.match(checkRegex)) return;
        // then we make sure there's actually a value there
        if(!this.config.specific[specificKey][stat]) return;

        stats[stat as Stat] = this.config.specific[specificKey][stat];
      });
    });

    return stats as Record<Stat, number>;
  }

}