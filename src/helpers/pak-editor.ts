
import * as fs from 'fs-extra';

import { Enemy, Stat } from '../models';

/*
finDirPath_BP = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\BP\\Enemy\\Zako\\Data\\'
finDirPath_Data = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\'
finDirPath_Boss = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\'
finDirPath_shinju = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\ShinjuStatusTableList\\'
finDirPath_parts = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\Parts\\'
*/

export interface IPakFileEditorOpts {
}

export class PakFileEditor {

  private fileCache: Record<string, Buffer> = {};
  
  constructor(private opts: IPakFileEditorOpts) {}

  public editHexForEnemy(enemy: Enemy) {

    // check if we have this file in cache already
    let file: Buffer = this.fileCache[enemy.uexpFilePath];
    if(!file) {
      file = fs.readFileSync(enemy.uexpFilePath);
      this.fileCache[enemy.uexpFilePath] = file;
    }

    // iterate through all the offsets and apply the multipliers
    Object.keys(enemy.offsets).forEach(offsetStat => {
      const statValue = file.readInt32LE(enemy.offsets[offsetStat as Stat]);
      let newStatValue = Math.floor(statValue * 100);

      if(newStatValue > 2147483647) newStatValue = 2147483647;

      file.writeInt32LE(newStatValue, enemy.offsets[offsetStat as Stat]);
    });
  }

  // flush all files to the build directory
  public flush() {
    Object.keys(this.fileCache).forEach(fileName => {
      console.log(fileName);
    });
  }

}