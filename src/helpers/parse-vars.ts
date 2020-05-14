
import * as path from 'path';

import { Enemy, EnemyType } from '../models';

export interface VarParserOptions {

  // the offset of where to start the parser
  offsetStart: number;

  // the number of bytes to increase the offset iterator by
  offsetIteratorIncrementBy: number;

  // the file path for the corresponding uexp file
  uexpFilePath: string;

  // the file path for the corresponding json file
  jsonFilePath: string;

  // the subfolder a file is placed in logically (used primarly for shinju)
  buildFolder?: string;

  // the enemy type matching this parser
  type: EnemyType;
}

export class EnemyParser {

  constructor(private opts: VarParserOptions) {}

  // parse the file baesd on what is passed into the parser
  public parse(): Enemy[] {

    // load the json file
    let enemiesInFile = [];
    try {
      enemiesInFile = require(path.join('..', '..', this.opts.jsonFilePath));
    } catch(e) {
      console.log(`Could not find file ${this.opts.jsonFilePath}. Skipping...`);
      return [];
    }

    return enemiesInFile

      // turn all enemies into Enemy objects
      .map((enemyData: any, enemyIndex: number) => {
        const name = enemyData.Value.Name_29_7A62483740A6D0DF1414CB9963F7CF87;

        // skip dummy enemies
        if(name === 'dummy') return;

        return new Enemy({
          id: enemyData.Key,
          uexpFilePath: this.opts.uexpFilePath,
          name,
          buildFolder: this.opts.buildFolder,
          type: this.opts.type,
          hpOffset: this.opts.offsetStart + (enemyIndex * this.opts.offsetIteratorIncrementBy)
        });
      })

      // filter out entries that are empty
      .filter(Boolean);

  }
}