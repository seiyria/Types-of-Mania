

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
  [EnemyType.Part]:     `Trials of Mana/Content/Game00/Data/Csv/CharaData/Parts`,
  [EnemyType.Shinju]:   `Trials of Mana/Content/Game00/Data/Csv/CharaData/ShinjuStatusTableList`,
}

export interface PakFileEditorOpts {
  configLoader: ConfigLoader;
  unrealPakLocation?: string;
  dumpStats?: boolean;
}

export class PakFileEditor {

  private fileCache: Record<string, Buffer> = {};
  private fileOutputLocation: Record<string, string> = {};

  private allEnemyStats: Record<string, Partial<Record<'name'|Stat, string|number>>> = {};
  
  constructor(private opts: PakFileEditorOpts) {}

  // edit the hex file for an individual enemy
  public editHexForEnemy(enemy: Enemy): void {

    const enemyUniqueId = `${enemy.uexpFilePath}|${enemy.id}`;
    this.allEnemyStats[enemyUniqueId] = { name: enemy.name };

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
    const enemyMultipliers = this.opts.configLoader.getStatMultipliers(enemy);

    // iterate through all the offsets and apply the multipliers
    Object.keys(enemy.offsets).forEach(offsetStat => {

      // get the value and multiply it by the multiplier
      const statValue = file.readInt32LE(enemy.offsets[offsetStat as Stat]);
      let newStatValue = Math.floor(statValue * enemyMultipliers[offsetStat as Stat]);

      // drop rates should _probably_ be 0-100
      if(offsetStat.includes('drop')) {
        newStatValue = Math.max(0, Math.min(100, newStatValue));
      }

      // we can't exceed int max (2^32 - 1) or int min
      newStatValue = Math.max(-2147483648, Math.min(2147483647, newStatValue));

      this.allEnemyStats[enemyUniqueId][offsetStat as Stat] = newStatValue;

      file.writeInt32LE(newStatValue, enemy.offsets[offsetStat as Stat]);
    });
  }

  // flush all files to the build directory
  public async flush(): Promise<void> {

    // the root build directory
    const fileRoot = `build/pak/${packageFile.version}`;

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

    let unrealPakLocation = this.opts.unrealPakLocation || `buildtools/UnrealPak.exe`

    // make sure the two build tools exist
    const doesExeExist = fs.pathExistsSync(unrealPakLocation);
    const doesBaseExist = fs.pathExistsSync('UnrealPak.exe');

    if(!doesExeExist && !doesBaseExist) {
      console.error(`Error: Could not find UnrealPak.exe. Please make sure it is placed alongside the exe or at buildtools/UnrealPak.exe or specify --unrealPak`);
      return;
    }

    if(doesBaseExist) {
      unrealPakLocation = 'UnrealPak.exe';
    }

    const buildRoot = `build/pak/${packageFile.version}`;
    const fullBuildRoot = path.resolve(buildRoot);

    const fullExeRoot = path.resolve(unrealPakLocation);

    // bundle all the files using UnrealPak
    console.log('Bundling...');
    fs.writeFileSync(`${buildRoot}/filelist.txt`, `"${fullBuildRoot}\\tmp\\*.*" "..\\..\\..\\*.*"`);
    childProcess.execSync(`"${fullExeRoot}" "${fullBuildRoot}\\TypesOfMania_P.pak" -Create="${fullBuildRoot}\\filelist.txt"`);

    // clean up files
    console.log('Cleaning up...');

    // we have to wait a bit because ???
    setTimeout(() => {
      fs.removeSync('Engine');
      fs.removeSync(`${fullBuildRoot}/filelist.txt`);
      fs.removeSync(`${buildRoot}/tmp`);

      fs.writeFileSync(`${buildRoot}/config.yml`, YAML.safeDump(this.opts.configLoader.finalConfig));
    }, 100);

    // dump in CSV if we need to
    if(this.opts.dumpStats) {
      const stats = ['id', 'name', ...Object.values(Stat)];
      let statString = stats.join(',') + '\n';
      Object.keys(this.allEnemyStats).forEach(enemyId => {
        const monStats = [
          enemyId, 
          this.allEnemyStats[enemyId].name,
          ...Object.values(Stat).map(s => this.allEnemyStats[enemyId][s])
        ];
        statString += monStats.join(',') + '\n';
      });

      fs.writeFileSync(`${buildRoot}/stats.csv`, statString);
    }

    // try automatic installation
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
    if(this.opts.dumpStats) {
      console.log('A dump of all monster stats has been included as stats.csv.');
    }
  }

}