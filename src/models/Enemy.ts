
export enum Stat {
  HP = 'hp',
  ATK = 'atk',
  DEF = 'def',
  AGI = 'agi',
  INT = 'int',
  SPR = 'spr',
  LUCK = 'luck',
  OFFMAG = 'offMag',
  DEFMAG = 'defMag',
  EXP = 'exp'
}

// TODO: ai, drop rates, drop items, lucre

export interface IEnemyOpts {

  // the uexp file path for this enemy
  uexpFilePath: string;

  // the enemy name
  name: string;

  // the hp offset for the enemy
  hpOffset: number;
}

export class Enemy {

  public get uexpFilePath(): string {
    return this.opts.uexpFilePath;
  }

  public get offsets(): Record<Stat, number> {
    return {
      hp:     this.opts.hpOffset,
      atk:    this.opts.hpOffset + (29 * 3),
      def:    this.opts.hpOffset + (29 * 4),
      agi:    this.opts.hpOffset + (29 * 5),
      int:    this.opts.hpOffset + (29 * 6),
      spr:    this.opts.hpOffset + (29 * 7),
      luck:   this.opts.hpOffset + (29 * 8),
      defMag: this.opts.hpOffset + (29 * 9),
      offMag: this.opts.hpOffset + (29 * 10),
      exp:    this.opts.hpOffset + (29 * 822),
    };
  }

  constructor(private opts: IEnemyOpts) {}

}