# Trials of Mania

A difficulty modifier tool for Trials of Mana. Credits to [pyroll](https://github.com/pyroll/Trials-of-Mania---Difficulty-Mod) for the original Python scripts that got this going.

## Features

* Allows for changing of the following stats via a multiplier: hp, mp, atk, def, agi, int, spr, luck, offMag, defMag, exp, lucre, drop1, drop2, drop3.
* Allows for global changes, or specific boss, monster, shinju, or part enemies.
* Allows for specific enemy changes for fine-tuning specific enemies using specific creature names or level ranges.
* Has a very simple build process, which allows for automatic installation to your mod directory.
* Supports a config file for easy sharing of configs.
* Supports CLI arguments for easy copy/paste setups.

## Usage

### CLI

The CLI allows you to specify custom overrides without messing with `config.yml`. It is very flexible, and lets you specify any key/subkey as follows:

* `--version` will just print the current version of the app.
* `--dumpData` will dump monster names and item names.
* `--config <config.yml>` will load a config from a specified path. Default: `config/config.yml`.
* `--unrealPak <UnrealPak.exe>` will search for UnrealPak.exe in the specified path. Default: `build/tools/UnrealPak/UnrealPak.exe`
* `--seed <num>` will set the RNG seed for randomizing. Default: completely random.
* `--installTo <path>` will automatically move the completed pak to your `~mod` folder. Default: `C:\Program Files (x86)\Steam\steamapps\common\Trials of Mana`.
* `--global.<stat> <multiplier>` will set the global `stat` multiplier to `multiplier` 
* `--boss.<stat> <multiplier>` will set the boss `stat` multiplier to `multiplier` 
* `--monster.<stat> <multiplier>` will set the monster `stat` multiplier to `multiplier` 
* `--shinju.<stat> <multiplier>` will set the shinju `stat` multiplier to `multiplier` 
* `--part.<stat> <multiplier>` will set the part `stat` multiplier to `multiplier` 

The valid `stat` keys you can set can be found in `config.yml`.

To pass these in to `npm start`, do this (for example): `npm start -- --global.xp 1 --global.hp 3` (notice the first set of `--` before the args are passed in).

### config.yml

The `config/config.yml` file can be modified to add any of the keys you would normally pass via the CLI. It also features the ability to single out specific monsters for scaling. For example, you could do this:

```yml
specific:
   MAGICIAN_LV16:
      exp: 10
```

This would make monsters that are `MAGICIAN_LV16` give 10x their normal exp. The name for the creature comes out of the JSON files in the `gamedata` folder.

You can also do this:

```yml
specific:
  lv[0-9][^0-9]:
    hp: 0.8
  
  lv[1][0-9]:
    hp: 3
```

This uses the enhanced feature for specifics that allows you to use regex to filter out a creature name and apply stats - it's somewhat like a filter. In this case, this would set the HP value to creatures level 0-9 to 80% of their max, and creatures from level 10-19 to 3x their max HP. This can be used to better fine-tune the stats for different level ranges.

### Finished Pak Files

Copy the built `TypesOfMania_P.pak` file from the `build` folder into the `Trials of Mana/Content/Paks/~mod` folder. If the `~mod` folder does not already exist, you'll have to make it. Alternatively, to do this automatically, you can use the `--installTo` option.

## Development

You need to install NodeJS. The latest version is always recommended.

### Setup

* `npm i`

### Commands

* `npm start` (runs the configurator with default config)

### Building

* `npm start` (runs the configurator with default config)

#### Included JSON Files

The JSON files included in this repo are built from a [Serializer from this project tailored towards Bloodstained](https://github.com/ithinkandicode/bloodstained-tools/tree/master/Serializer). They're included because it's much easier than having to extract them.

#### UnrealPak

We can't bundle UnrealPak with this repo, but you can get it from [here](https://mega.nz/file/BY0gUIqI#rYaUGom59yFDLNGtwai1W_QSeLZDIEd3qFbeApJ5f3Q) (link courtesy of the Bloodstained discord). 

Unzip the file and grab `Tools/UnrealPak` folder and put it in `build/tools` (the directory may have to be created). The final folder structure should be `build/tools/UnrealPak` with the `.exe` and `.bat` files in that folder.

## Future Features

* Verbose stat edit logs
* Part-type enemies working (they might already work???)
* Edit healing item potency
* Item shop randomizer (w/ seeds)
* Item randomization (w/ seeds)
* Item drop randomization (w/ seeds)
* Monster randomization (w/ seeds)
* Monster ability randomization (w/ seeds)
* Item-specific drop rate multiplier boosts
* Tests

If you or someone you know can help get the Bloodstained Serializer working in reverse to turn these `json` files back into `uexp` files, that would be immensely helpful.

## Warning

This tool modifies your games data, and while the mod can be reversed, if it does damage to your save file, this tool is not responsible for that.