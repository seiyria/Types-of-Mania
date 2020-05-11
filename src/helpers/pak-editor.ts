

import * as fs from 'fs-extra';
import * as YAML from 'js-yaml';
import * as path from 'path';
import * as childProcess from 'child_process';

import { Enemy, Stat, EnemyType } from '../models';
import { ConfigLoader } from './config-loader';

import * as packageFile from '../../package.json';

// where files for each enemy type go
const FILE_LOCATIONS: Record<EnemyType, string> = {
  [EnemyType.Boss]:     `Trials of Mana/Content/Game00/Data/Csv/CharaData`,
  [EnemyType.Monster]:  `Trials of Mana/Content/Game00/BP/Enemy/Zako/Data`,
  [EnemyType.Part]:     `Trials of Mana/Content/Game00/Data/Csv/CharaData/PartsList`,
  [EnemyType.Shinju]:   `Trials of Mana/Content/Game00/Data/Csv/CharaData/ShinjuStatusTableList`,
}

export interface PakFileEditorOpts {
  configLoader: ConfigLoader;
}

export class PakFileEditor {

  private fileCache: Record<string, Buffer> = {};
  private fileOutputLocation: Record<string, string> = {};
  
  constructor(private opts: PakFileEditorOpts) {}

  // edit the hex file for an individual enemy
  public editHexForEnemy(enemy: Enemy): void {

    const fileKey = path.basename(enemy.uexpFilePath);

    // check if we have this file in cache already
    let file: Buffer = this.fileCache[fileKey];

    // if not, grab it & cache it
    if(!file) {
      file = fs.readFileSync(enemy.uexpFilePath);
      this.fileCache[fileKey] = file;
      this.fileOutputLocation[fileKey] = FILE_LOCATIONS[enemy.type];
    }

    // get the multipliers for this specific enemy
    const enemyMultipliers = this.opts.configLoader.getStats(enemy);

    // iterate through all the offsets and apply the multipliers
    Object.keys(enemy.offsets).forEach(offsetStat => {
      const statValue = file.readInt32LE(enemy.offsets[offsetStat as Stat]);
      let newStatValue = Math.floor(statValue * enemyMultipliers[offsetStat as Stat]);

      // we can't exceed int max (2^32 - 1)
      if(newStatValue > 2147483647) newStatValue = 2147483647;

      file.writeInt32LE(newStatValue, enemy.offsets[offsetStat as Stat]);
    });
  }

  // flush all files to the build directory
  public flush(): void {

    // the root build directory
    const fileRoot = `build/${packageFile.version}`;

    // clear out old temporary files
    fs.removeSync(`${fileRoot}/tmp`);

    // create each file from memory
    Object.keys(this.fileCache).forEach(async fileName => {
      const path = `${fileRoot}/tmp/${this.fileOutputLocation[fileName]}`;
      await fs.ensureDir(path);
      await fs.writeFile(`${path}/${fileName}`, this.fileCache[fileName]);
    });

    this.pack();
  }

  // pack the files using UnrealPak
  public async pack(): Promise<void> {
    // make sure the folder exists
    await fs.ensureDir(`build/tools/UnrealPak`);

    // make sure the two build tools exist
    const doesExeExist = await fs.pathExists(`build/tools/UnrealPak/UnrealPak.exe`);
    const doesBatExist = await fs.pathExists(`build/tools/UnrealPak/UnrealPak-Without-Compression.bat`);

    if(!doesExeExist) {
      console.error(`Error: Could not find UnrealPak.exe. Please make sure it is placed in build/tools/UnrealPak`);
    }

    if(!doesBatExist) {
      console.error(`Error: Could not find UnrealPak-Without-Compression.bat. Please make sure it is placed in build/tools/UnrealPak`);
    }

    if(!doesExeExist || !doesBatExist) return;

    const fileRoot = `build/${packageFile.version}/tmp/Trials of Mana`;
    const fullRoot = path.resolve(fileRoot);
    const fullBatRoot = path.resolve('build/tools/UnrealPak/UnrealPak-Without-Compression.bat');

    // bundle all the files using UnrealPak
    console.log('Bundling...');
    childProcess.execSync(`"${fullBatRoot}" "${fullRoot}"`);

    // clean up files
    console.log('Cleaning up...');

    // we have to wait a bit because ???
    setTimeout(() => {
      fs.copyFileSync(`build/${packageFile.version}/tmp/Trials of Mana.pak`, `build/${packageFile.version}/Trials of Mana.pak`)

      fs.removeSync('Engine');
      fs.removeSync('build/tools/UnrealPak/filelist.txt');
      fs.removeSync(`build/${packageFile.version}/tmp`);

      fs.writeFileSync(`build/${packageFile.version}/config.yml`, YAML.safeDump(this.opts.configLoader.finalConfig));
    }, 100);

    // we're done!
    console.log(`Done! Your built pak file is located at build/${packageFile.version}/Trials of Mana.pak`);
    console.log('A copy of the config file that created this build has been included for reference.');
  }

}