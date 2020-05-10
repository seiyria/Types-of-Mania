
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
    let file: Buffer = this.fileCache[enemy.uexpFilePath];
    if(!file) {
      file = fs.readFileSync(enemy.uexpFilePath);
      this.fileCache[enemy.uexpFilePath] = file;
    }

    Object.keys(enemy.offsets).forEach(offsetStat => {
      console.log(offsetStat, 
        file[enemy.offsets[offsetStat as Stat]], 
        file.readUInt32LE(enemy.offsets[offsetStat as Stat]));
    });

    console.log(enemy, file);
  }

}