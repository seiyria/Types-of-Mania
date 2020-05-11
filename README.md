# Trials of Mania

A difficulty modifier tool for Trials of Mana.

## Features

* Allows for changing of the following stats via a multiplier: hp, atk, def, agi, int, spr, luck, offMag, defMag, exp.
* Allows for global changes, or specific boss, monster, shinju, or part enemies.
* Allows for specific enemy changes for fine-tuning specific enemies.
* Has a very simple build process.
* Supports a config file for easy sharing of configs.
* Supports CLI arguments for easy copy/paste setups.

## Usage

### CLI

The CLI allows you to specify custom overrides without messing with `config.yml`. It is very flexible, and lets you specify any key/subkey as follows:

* `--seed <num>` will set the RNG seed for randomizing.
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

### Finished Pak Files

Copy the built pak file from the `TrialsOfMania` folder into a `~mod` folder.

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

* Parts working
* Shinju working
* Lucre multiplier
* Item drop rate multiplier
* Item shop randomizer (w/ seeds)
* Item randomization (w/ seeds)
* Item drop randomization (w/ seeds)
* Monster randomization (w/ seeds)
* Monster ability randomization (w/ seeds)

## Version History

- Version 0.4
   - Rewrite to JS.
   - Support config files, CLI arguments.
   - Update build process to output a pak file w/ the associated config.

- Version 0.3
   - pars.py files are still horribly done and need to be reworked, might wait until after I add the rest of the data files to the mod in the next update.
   - At some point it'd be nice to store all of the class instance stuff as data in a json file instead of copy pasting them all onto the main ene_clas.py script.