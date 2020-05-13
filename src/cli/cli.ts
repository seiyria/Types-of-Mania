

import packageFile from '../../package.json';

import { BossParsers, NormalEnemyParsers, ShinjuParsers } from '../parsers';
import { ConfigLoader, PakFileEditor, AssetLoader } from '../helpers';

// eslint-disable-next-line @typescript-eslint/no-var-requires
const argv = require('minimist')(process.argv.slice(2));
delete argv._;

if(argv.version) {
  console.log(`v${packageFile.version}`);
  process.exit(0);
}

if(argv.dumpData) {
  const assetLoader = new AssetLoader();
  assetLoader.flush();
  process.exit(0);
}

const { config, configJson, unrealPak, ...totalConfig } = argv;

// set up the config / pak file editor
const configLoader = new ConfigLoader({ overrides: totalConfig, configLocation: config, configJson });
const editor = new PakFileEditor({ configLoader, unrealPakLocation: unrealPak });

// get all of the enemies
const bossEnemies = BossParsers.map(x => x.parse()).flat();
const normalEnemies = NormalEnemyParsers.map(x => x.parse()).flat();
const shinjuEnemies = ShinjuParsers.map(x => x.parse()).flat();

// edit their hex files (in memory)
bossEnemies.forEach(e => editor.editHexForEnemy(e));
normalEnemies.forEach(e => editor.editHexForEnemy(e));
shinjuEnemies.forEach(e => editor.editHexForEnemy(e));

// flush the uexp files to disk
editor.flush();