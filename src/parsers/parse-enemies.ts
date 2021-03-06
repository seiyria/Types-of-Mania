
import * as fs from 'fs-extra';
import * as path from 'path';

import { EnemyParser } from '../helpers';
import { EnemyType } from '../models';

const allFiles = fs
  .readdirSync(path.join(__dirname, '..', '..', 'gamefiles', 'enemy', 'uexp'))
  .map(f => path.basename(f, '.uexp'));

export const NormalEnemyParsers = allFiles.map(fileName => {
  return new EnemyParser({
    offsetStart: 111,
    offsetIteratorIncrementBy: 1579,
    type: EnemyType.Monster,
    uexpFilePath: `gamefiles/enemy/uexp/${fileName}.uexp`,
    jsonFilePath: `gamefiles/enemy/json/${fileName}.json`
  });
});