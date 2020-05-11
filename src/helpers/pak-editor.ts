

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

      if(enemy.buildFolder) {
        this.fileOutputLocation[fileKey] = `${this.fileOutputLocation[fileKey]}/${enemy.buildFolder}`;
      }
    }

    // get the multipliers for this specific enemy
    const enemyMultipliers = this.opts.configLoader.getStats(enemy);

    // iterate through all the offsets and apply the multipliers
    Object.keys(enemy.offsets).forEach(offsetStat => {
      const statValue = file.readInt32LE(enemy.offsets[offsetStat as Stat]);
      let newStatValue = Math.floor(statValue * enemyMultipliers[offsetStat as Stat]);

      // we can't exceed int max (2^32 - 1)
      if(newStatValue > 2147483647) newStatValue = 2147483647;

      // safe-guard so we can't set HP to 0 (I imagine this works)
      if(offsetStat === Stat.HP && newStatValue <= 0) newStatValue = 1;

      file.writeInt32LE(newStatValue, enemy.offsets[offsetStat as Stat]);
    });
  }

  // flush all files to the build directory
  public async flush(): Promise<void> {

    // the root build directory
    const fileRoot = `build/${packageFile.version}`;

    // clear out old temporary files
    fs.removeSync(`${fileRoot}/tmp`);

    // create each file from memory
    await Promise.all(Object.keys(this.fileCache).map(async fileName => {
      const path = `${fileRoot}/tmp/${this.fileOutputLocation[fileName]}`;
      await fs.ensureDir(path);
      await fs.writeFile(`${path}/${fileName}`, this.fileCache[fileName]);
    }));

    this.pack();
  }

  // pack the files using UnrealPak
  public async pack(): Promise<void> {
    // make sure the folder exists
    await fs.ensureDir(`build/tools/UnrealPak`);

    // make sure the two build tools exist
    const doesExeExist = await fs.pathExists(`build/tools/UnrealPak/UnrealPak.exe`);

    if(!doesExeExist) {
      console.error(`Error: Could not find UnrealPak.exe. Please make sure it is placed in build/tools/UnrealPak`);

      return;
    }

    const buildRoot = `build/${packageFile.version}`;
    const fullBuildRoot = path.resolve(buildRoot);

    const fullExeRoot = path.resolve('build/tools/UnrealPak/UnrealPak.exe');

    // bundle all the files using UnrealPak
    console.log('Bundling...');
    fs.writeFileSync(`${buildRoot}/filelist.txt`, `"${fullBuildRoot}\\tmp\\*.*" "..\\..\\..\\*.*"`);
    childProcess.execSync(`"${fullExeRoot}" "${fullBuildRoot}\\TypesOfMania_P.pak" -Create=${fullBuildRoot}\\filelist.txt`);

    // clean up files
    console.log('Cleaning up...');

    // we have to wait a bit because ???
    setTimeout(() => {
      fs.removeSync('Engine');
      fs.removeSync(`${fullBuildRoot}/filelist.txt`);
      // fs.removeSync(`${buildRoot}/tmp`);

      fs.writeFileSync(`${buildRoot}/config.yml`, YAML.safeDump(this.opts.configLoader.finalConfig));
    }, 100);

    const installTo = this.opts.configLoader.finalConfig.installTo;
    if(installTo) {
      if(fs.pathExistsSync(installTo)) {
        console.log(`Installing directly to ${installTo}...`);
        
        const finalInstallDir = `${installTo}/Trials of Mana/Content/Paks/~mod`;
        await fs.ensureDirSync(finalInstallDir);

        fs.copyFileSync(`${buildRoot}/TypesOfMania_P.pak`, `${finalInstallDir}/TypesOfMania_P.pak`);
        fs.writeFileSync(`${finalInstallDir}/TypesOfMania_config.yml`, YAML.safeDump(this.opts.configLoader.finalConfig));

      } else {
        console.log(`Tried to install directly to ${installTo} but failed (directory does not exist). Skipping...`);

      }
    }

    // we're done!
    console.log(`Done! Your built pak file is located at ${buildRoot}/TypesOfMania_P.pak`);
    console.log('A copy of the config file that created this build has been included for reference.');
  }

}