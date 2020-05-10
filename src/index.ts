
import { Parsers as NormalEnemyParsers } from './parsers/parse-enemies';
import { Parsers as BossParsers } from './parsers/parse-boss';

console.log(NormalEnemyParsers.map(x => x.parse().map(x => (x as any).opts)));
console.log(BossParsers.map(x => x.parse().map(x => (x as any).opts)));