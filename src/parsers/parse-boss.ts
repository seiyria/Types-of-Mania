
import { EnemyParser } from '../helpers';
import { EnemyType } from '../models';

export const BossParsers = [new EnemyParser({
  offsetStart: 140,
  offsetIteratorIncrementBy: 1624,
  type: EnemyType.Boss,
  uexpFilePath: `gamefiles/boss/uexp/chardata/BossStatusTable.uexp`,
  jsonFilePath: `gamefiles/boss/json/chardata/_BossStatusTable.json`
})];