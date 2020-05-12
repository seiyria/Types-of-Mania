# Types of Mania
----------------

This mod is based off of rollcall's excellent rebalance mod. It adds more features on top of the base mod.

# Features
----------
* Supports a config file (config/config.yml) which can be edited/shared to make creating custom builds more easily
* Supports more stats (full listing below)
* Supports specific enemy overrides
* Supports ranges of enemy overrides
* Can automatically install to your Trials of Mana ~mod directory
* Has a flexible CLI that mirrors the config.yml fields

# Default Stat Changes
----------------------

The default stat changes mirror rollcall's mod, but other stats are untested.

Base Stats:

* HP -> 200%
* MP -> 100%
* ATK -> 150%
* DEF -> 100%
* AGI -> 120%
* INT -> 150%
* SPR -> 150%

Secondary Stats:

* Exp -> 100%
* Lucre -> 100%
* Drop Rate (Item 1) -> 100%
* Drop Rate (Item 2) -> 100%
* Drop Rate (Item 3) -> 100%

Other Stats:

* OffMag -> 100%
* DefMag -> 100%

SPP Stats:

* DropSpp -> 100%
* KnockoutDropSpp -> 100%
* LAttackDropSpp -> 100%
* ChargeAttackDropSpp -> 100%

# Default Usage
---------------

Copy TypesOfMania_P.pak to your ~mod folder. It is probably located 
here: C:\Program Files (x86)\Steam\steamapps\common\Trials of Mana\Trials of Mana\Content\Paks\~mod.

# Custom Usage
--------------

First, you'll need to get UnrealPak.exe. You can get that from this 
link: https://mega.nz/file/VVlwwCLL#TDBl3WBB2uEHKFhiXpLdynRZ6irUiLW82HmltmoTW8M

Second, you'll need to put that next to the types-of-mania-win.exe file.

Then, you can run the CLI with any arguments (detailed below), but by default, you can run 
the exe file and it will create a .pak file in build/pak/${version}

# CLI Arguments
---------------
The CLI allows you to specify custom overrides without messing with `config.yml`. 
It is very flexible, and lets you specify any key/subkey as follows:

* `--version` will just print the current version of the app.

* `--dumpData` will dump monster names and item names.

* `--config <config.yml>` will load a config from a specified path. 
  Default: `config/config.yml`.

* `--unrealPak <UnrealPak.exe>` will search for UnrealPak.exe in the specified path. 
  Default: `buildtools/UnrealPak.exe` or `UnrealPak.exe`.

* `--seed <num>` will set the RNG seed for randomizing. Default: completely random.

* `--installTo <path>` will automatically move the completed pak to your `~mod` folder. 
  Default: `C:\Program Files (x86)\Steam\steamapps\common\Trials of Mana`.

* `--global.<stat> <multiplier>` will set the global `stat` multiplier to `multiplier`.

* `--boss.<stat> <multiplier>` will set the boss `stat` multiplier to `multiplier`.

* `--monster.<stat> <multiplier>` will set the monster `stat` multiplier to `multiplier`.

* `--shinju.<stat> <multiplier>` will set the shinju `stat` multiplier to `multiplier`.

* `--part.<stat> <multiplier>` will set the part `stat` multiplier to `multiplier`.

The valid `stat` keys you can set can be found in `config.yml`.

# Custom config.yml Changes
---------------------------

Outside of simple categories like boss and enemy, there is also a `specific` block in config.yml 
which supports custom overrides for specific monsters and ranges of monsters.

For example, if you do this:

specific:
  MAGICIAN_LV16:
    exp: 10

It will make creatures with the id matching MAGICIAN_LV16 give 10x their normal exp. 
This can be expanded in a more powerful way, like so:

specific:
  lv[0-9][^0-9]:
    hp: 0.8

This is a regular expression, which in this case, means it applies to multiple enemies.
This particular expression means anything that says "lv0,lv1,lv2,lv3,lv4,lv5,lv6,lv7,lv8,lv9" -
which means it will match any enemy whose level is less than 10 (and make their HP 80%).

We can apply this again to get creatures for levels 10-19 like so:

specific:
  lv[1][0-9]:
    hp: 3

This will apply to all creatures level 10-19, and make their HP 300%.

# GitHub Repository
-------------------

The GitHub repo has more information: https://github.com/seiyria/Types-of-Mania as well as more frequent releases.