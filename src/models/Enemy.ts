
export enum EnemyType {
  Boss = 'boss',
  Monster = 'monster',
  Shinju = 'shinju',
  Part = 'part'
}

export enum Stat {
  HP = 'hp',
  MP = 'mp',
  ATK = 'atk',
  DEF = 'def',
  AGI = 'agi',
  INT = 'int',
  SPR = 'spr',
  LUCK = 'luck',

  OFFMAG = 'offMag',
  DEFMAG = 'defMag',

  EXP = 'exp',
  DROPSPP = 'dropSpp',
  LUCRE = 'lucre',

  DROP1 = 'drop1',
  DROP2 = 'drop2',
  DROP3 = 'drop3',

  KODROPSPP = 'knockoutDropSpp',
  LATTDROPSPP = 'lAttackDropSpp',
  CHARGEDROPSPP = 'chargeAttackDropSpp'
}

/*


    if(enemy.name === 'RABI_Lv1' || enemy.name === 'GOBLINLORD_LV40') {
      console.log(enemy.name, enemy.offsets)
    }
    */

export interface EnemyOpts {

  // the uexp file path for this enemy
  uexpFilePath: string;

  // the optional build folder for this enemy (used mostly for shinju)
  buildFolder?: string;

  // the enemy name
  name: string;

  // the hp offset for the enemy
  hpOffset: number;

  // the type of enemy
  type: EnemyType;
}

export class Enemy {

  public get name(): string {
    return this.opts.name;
  }

  public get buildFolder(): string {
    return this.opts.buildFolder || '';
  }

  public get type(): EnemyType {
    return this.opts.type;
  }

  public get uexpFilePath(): string {
    return this.opts.uexpFilePath;
  }

  // these are all the offsets I have for the number data
  // if it's commented out, I don't know what it's useful for
  // the data in the offset record is presented in order
  public get offsets(): Record<Stat, number> {
    return {
      hp:                   this.opts.hpOffset,
      mp:                   this.opts.hpOffset + (      29 * 1),
      // technique:  this.opts.hpOffset + (     29 * 2),
      atk:                  this.opts.hpOffset + (      29 * 3),
      def:                  this.opts.hpOffset + (      29 * 4),
      agi:                  this.opts.hpOffset + (      29 * 5),
      int:                  this.opts.hpOffset + (      29 * 6),
      spr:                  this.opts.hpOffset + (      29 * 7),
      luck:                 this.opts.hpOffset + (      29 * 8),
      defMag:               this.opts.hpOffset + (      29 * 9),
      offMag:               this.opts.hpOffset + (      29 * 10),
      
      exp:                  this.opts.hpOffset + (822),
      dropSpp:              this.opts.hpOffset + (822 + 29 * 1),

      drop1:                this.opts.hpOffset + (953),
      drop2:                this.opts.hpOffset + (957),
      drop3:                this.opts.hpOffset + (961),

      lucre:                this.opts.hpOffset + (990),

      // enemyClass: this.opts.hpOffset + (990 + 29 * 1)
      knockoutDropSpp:      this.opts.hpOffset + (990 + 29 * 2),
      lAttackDropSpp:       this.opts.hpOffset + (990 + 29 * 3),
      chargeAttackDropSpp:  this.opts.hpOffset + (990 + 29 * 4)
    };
  }

  constructor(private opts: EnemyOpts) {}

}