
import * as fs from 'fs-extra';
import * as path from 'path';

import { EnemyParser } from '../helpers';
import { EnemyType } from '../models';

const allFiles = fs
  .readdirSync(path.join(__dirname, '..', '..', 'gamefiles', 'boss', 'uexp', 'parts'))
  .map(f => path.basename(f, '.uexp'));

export const PartParsers = allFiles.map(fileName => {
  return new EnemyParser({
    offsetStart: 111,
    offsetIteratorIncrementBy: 1579,
    type: EnemyType.Monster,
    uexpFilePath: `gamefiles/boss/uexp/parts/${fileName}.uexp`,
    jsonFilePath: `gamefiles/boss/json/parts/${fileName}.json`
  });
});