
import * as path from 'path';

import { Enemy } from '../models';

export interface IVarParserOptions {

  // the offset of where to start the parser
  offsetStart: number;

  // the number of bytes to increase the offset iterator by
  offsetIteratorIncrementBy: number;

  // the file path for the corresponding uexp file
  uexpFilePath: string;

  // the file path for the corresponding json file
  jsonFilePath: string;
}

export class EnemyParser {

  constructor(private opts: IVarParserOptions) {}

  // parse the file baesd on what is passed into the parser
  public parse(): Enemy[] {

    // load the json file
    let enemiesInFile = [];
    try {
      enemiesInFile = require(path.join('..', '..', this.opts.jsonFilePath));
    } catch(e) {
      console.error(`Could not find file ${this.opts.jsonFilePath}. Skipping...`);
      return [];
    }

    return enemiesInFile

      // turn all enemies into Enemy objects
      .map((enemyData: any, enemyIndex: number) => {
        const internalId = enemyData.Key;
        const name = enemyData.Value.Name_29_7A62483740A6D0DF1414CB9963F7CF87;

        const fullName = `${name} (${internalId})`;

        // skip dummy enemies
        if(name === 'dummy') return;

        return new Enemy({
          uexpFilePath: this.opts.uexpFilePath,
          name: fullName,
          hpOffset: this.opts.offsetStart + (enemyIndex * this.opts.offsetIteratorIncrementBy)
        });
      })

      // filter out entries that are empty
      .filter(Boolean);

  }
}