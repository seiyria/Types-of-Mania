
import * as fs from 'fs-extra';
import * as path from 'path';
import * as YAML from 'js-yaml';
import deepmerge from 'deepmerge';

import { Enemy, Stat } from '../models';

export interface IConfig {
  version: number;

  seed: number;

  global: Record<Stat, number>;
  boss: Record<Stat, number>;
  monster: Record<Stat, number>;
  shinju: Record<Stat, number>;
  part: Record<Stat, number>;

  specific: Record<string, Record<Stat, number>>;
}

export interface IConfigOpts {
  overrides: Partial<IConfig>;
}

export class ConfigLoader {

  private config!: IConfig;
  
  constructor(private opts: IConfigOpts) {
    this.init();
  }

  private init() {
    try {
      const config = YAML.safeLoad(fs.readFileSync(path.join(__dirname, '..', '..', 'config', 'config.yml')).toString());

      // if you specify override.global, copy those values to the other sections
      if(this.opts.overrides) {
        Object.keys(this.opts.overrides.global || {}).forEach(key => {
          ['boss', 'monster', 'shinju', 'part'].forEach(masterKey => {
            (this.opts.overrides as any)[masterKey] = (this.opts.overrides as any)[masterKey] || {};
            (this.opts.overrides as any)[masterKey][key] = (this.opts.overrides as any).global[key];
          });
        });
      }
  
      this.config = deepmerge(config, this.opts.overrides || {});
    } catch(e) {
      console.error(`Could not find config.yml in config/. Please place one there.`);
      process.exit(1);
    }
  }

  public getStats(enemy: Enemy): Record<Stat, number> {
    const type = this.config[enemy.type] || {};
    const specific = this.config.specific[enemy.name] || {};

    const stats: any = {};

    Object.values(Stat).forEach(stat => {
      stats[stat as Stat] = specific[stat] || type[stat] || 1;
    });

    return stats as Record<Stat, number>;
  }

}