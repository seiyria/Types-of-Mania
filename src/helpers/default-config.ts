
import deepmerge from 'deepmerge';

import { ModConfig } from './config-loader';

// this mirrors config.yml
const defaultStatConfig = {
  hp: 2,
  mp: 1,
  atk: 1.5,
  def: 1,
  agi: 1.2,
  int: 1.5,
  spr: 1.5,
  luck: 1,
  defMag: 1.3,
  offMag: 1.3,
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
  installTo: '',
  base: defaultStatConfig,
  boss: undefined,
  monster: undefined,
  shinju: undefined,
  specific: {}
};

export const getDefaultConfig = () => deepmerge({}, defaultConfig);