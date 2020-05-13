
import recursiveReadDir from 'fs-readdir-recursive';
import * as path from 'path';

import { EnemyParser } from '../helpers';
import { EnemyType } from '../models';

const allFiles = recursiveReadDir(
    path.join(__dirname, '..', '..', 'gamefiles', 'boss', 'uexp' ,'shinjustatustablelist')
  )
  .map(f => path.join(path.dirname(f), path.basename(f, '.uexp')));

export const ShinjuParsers = [
  ...allFiles
    .filter(fileName => !fileName.includes('Parts'))
    .map(fileName => {
      return new EnemyParser({
        offsetStart: 140,
        offsetIteratorIncrementBy: 1624,
        type: EnemyType.Shinju,
        uexpFilePath: `gamefiles/boss/uexp/shinjustatustablelist/${fileName}.uexp`,
        jsonFilePath: `gamefiles/boss/json/shinjustatustablelist/${fileName}.json`,
        buildFolder: path.dirname(fileName) !== '.' ? path.dirname(fileName) : ''
      });
    }),
    ...allFiles
      .filter(fileName => fileName.includes('Parts'))
      .map(fileName => {
        return new EnemyParser({
          offsetStart: 111,
          offsetIteratorIncrementBy: 1579,
          type: EnemyType.Shinju,
          uexpFilePath: `gamefiles/boss/uexp/shinjustatustablelist/${fileName}.uexp`,
          jsonFilePath: `gamefiles/boss/json/shinjustatustablelist/${fileName}.json`,
          buildFolder: path.dirname(fileName) !== '.' ? path.dirname(fileName) : ''
        });
      })
]