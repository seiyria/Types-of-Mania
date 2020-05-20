
import deepmerge from 'deepmerge';

import { ModConfig } from './config-loader';

// this mirrors config.yml
const defaultStatConfig = {
  hp: 2,
  mp: 1,
  atk: 1.5,
  def: 1,
  agi: 1,
  int: 1,
  spr: 1,
  luck: 1,
  defMag: 1.3,
  offMag: 1.3,
  downDurable: 1,
  guardDurable: 1,
  exp: 0.8,
  lucre: 1,
  drop1: 1,
  drop2: 1,
  drop3: 1,
  dropSpp: 1,
  knockoutDropSpp: 1,
  lAttackDropSpp: 1,
  chargeAttackDropSpp: 1
};

const defaultConfig: ModConfig = {
  version: 1,
  seed: 0,
  pakName: 'TypesOfMania_P',
  installTo: '',
  base: defaultStatConfig,
  boss: undefined,
  monster: undefined,
  shinju: undefined,
  part: undefined,
  specific: {}
};

export const getDefaultConfig: () => ModConfig = () => deepmerge({}, defaultConfig);