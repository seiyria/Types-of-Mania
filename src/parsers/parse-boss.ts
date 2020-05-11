
import { EnemyParser } from '../helpers';
import { EnemyType } from '../models';

export const BossParsers = [new EnemyParser({
  offsetStart: 140,
  offsetIteratorIncrementBy: 1624,
  type: EnemyType.Boss,
  uexpFilePath: `gamefiles/boss/uexp/charadata/BossStatusTable.uexp`,
  jsonFilePath: `gamefiles/boss/json/charadata/BossStatusTable.json`
})];