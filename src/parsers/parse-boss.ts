
import { EnemyParser } from '../helpers';

export const BossParsers = [new EnemyParser({
  offsetStart: 140,
  offsetIteratorIncrementBy: 1624,
  uexpFilePath: `gamefiles/boss/uexp/chardata/BossStatusTable.uexp`,
  jsonFilePath: `gamefiles/boss/json/chardata/_BossStatusTable.json`
})]