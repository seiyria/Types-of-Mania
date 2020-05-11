
const argv = require('minimist')(process.argv.slice(2));
delete argv._;

import { PakFileEditor } from '../helpers/pak-editor';

import { BossParsers, NormalEnemyParsers } from '../parsers';
import { ConfigLoader } from '../helpers';

const configLoader = new ConfigLoader({ overrides: argv });
const editor = new PakFileEditor({ configLoader });

const bossEnemies = BossParsers.map(x => x.parse()).flat();
const normalEnemies = NormalEnemyParsers.map(x => x.parse()).flat();

bossEnemies.forEach(e => editor.editHexForEnemy(e));
normalEnemies.forEach(e => editor.editHexForEnemy(e));

editor.flush();