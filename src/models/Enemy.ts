
export enum EnemyType {
  Boss = 'boss',
  Monster = 'monster',
  Shinju = 'shinju',
  Part = 'part'
}

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
      exp:    this.opts.hpOffset + (822),
    };
  }

  constructor(private opts: EnemyOpts) {}

}