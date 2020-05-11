# Trials of Mania

A difficulty modifier tool for Trials of Mana.

## Features

* Allows for changing of the following stats via a multiplier: hp, atk, def, agi, int, spr, luck, offMag, defMag, exp.

## Usage

### CLI

The CLI allows you to specify custom overrides without messing with `config.yml`. It is very flexible, and lets you specify any key/subkey as follows:

* `--seed <num>` will set the RNG seed for randomizing.
* `--global.<stat> <num>` will set the global `stat` to `num` 
* `--boss.<stat> <num>` will set the boss `stat` to `num` 
* `--monster.<stat> <num>` will set the monster `stat` to `num` 
* `--shinju.<stat> <num>` will set the shinju `stat` to `num` 
* `--part.<stat> <num>` will set the part `stat` to `num` 

The valid `stat` keys you can set can be found in `config.yml`.

### Finished Pak Files

Copy the built pak file from the `TrialsOfMania` folder into a `~mod` folder.

## Development

You need to install NodeJS. The latest version is always recommended.

### Setup

* `npm i`

### Commands

* `npm start` (runs the configurator with default config)

### Building

Yada yada, npm do stuff. Requires Windows because of UnrealPak.

#### Included JSON Files

The JSON files included in this repo are built from a [Serializer from this project tailored towards Bloodstained](https://github.com/ithinkandicode/bloodstained-tools/tree/master/Serializer). They're included because it's much easier than having to extract them.

#### UnrealPak

We can't bundle UnrealPak with this repo, but you can get it from [here](https://mega.nz/file/BY0gUIqI#rYaUGom59yFDLNGtwai1W_QSeLZDIEd3qFbeApJ5f3Q) (link courtesy of the Bloodstained discord). More instructions on where to place this coming later.

## Future Features

* Parts working
* Shinju working
* Specify different multipliers for individual creatures (TODO: come up with a sane naming scheme that uniquely identifies each creature/level combo)
* Lucre multiplier
* Item drop rate multiplier
* Item randomization (w/ seeds)
* Item drop randomization (w/ seeds)
* Monster randomization (w/ seeds)
* Monster ability randomization (w/ seeds)

## Version History

- Version 0.3 Update
   - pars.py files are still horribly done and need to be reworked, might wait until after I add the rest of the data files to the mod in the next update.
   - At some point it'd be nice to store all of the class instance stuff as data in a json file instead of copy pasting them all onto the main ene_clas.py script.