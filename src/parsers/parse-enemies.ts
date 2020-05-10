
import * as fs from 'fs';
import * as path from 'path';

import { EnemyParser } from '../helpers/parse-vars';

const allFiles = fs.readdirSync(path.join(__dirname, '..', '..', 'gamefiles', 'enemy', 'uexp'))
  .map(f => path.basename(f, '.uexp'));

export const Parsers = allFiles.map(fileName => {
  return new EnemyParser({
    offsetStart: 111,
    offsetIteratorIncrementBy: 1579,
    uexpFilePath: `gamefiles/enemy/uexp/${fileName}.uexp`,
    jsonFilePath: `gamefiles/enemy/json/_${fileName}.json`
  });
});