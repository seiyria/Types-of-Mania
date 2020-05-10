

import { PakFileEditor } from './helpers/pak-editor';

import { BossParsers, NormalEnemyParsers } from './parsers';

// console.log(NormalEnemyParsers.map(x => x.parse().map(x => (x as any).opts)));
// console.log(BossParsers.map(x => x.parse().map(x => (x as any).opts)));

const normalEnemies = NormalEnemyParsers.map(x => x.parse()).flat();

const editor = new PakFileEditor({});
editor.editHexForEnemy(normalEnemies[0]);

