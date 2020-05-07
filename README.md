# Trials-of-Mania---Difficulty-Mod

Apologies in advance for incorrect terminology.

The "Game Files" directory holds both the input and output files for the scripts. The "Boss" subdirectory contains the files used by "bos_clas.py", "bos_parse.py", "shinju_clas.py", and "shinju_pars.py". The other two, "JSON for viewing" and "uexp files" subdirs hold the files used by "ene_clas.py" and "ene_pars.py".

The " _clas.py" files aim to create an Enemy object that will hold offset locations for each stat of each Enemy instance that is created.
These offset locations point the editHexAll function to the index at which it will make edits to byte data in whatever 'uexp' file it is currently working with. Each instance is added to the 'enemyInstList' array which is looped through in the editHexAll function.

editHexAll function:
It grabs the full pathname of each file from 'rootdir', reads it as byte data, which is then assigned to 'mutableBytes' as a mutable bytearray. Each element (enemy) in 'enemyInstList' is iterated through and each offset attribute is used to grab the four bytes we need to edit. Those four bytes are converted to an integer, multiplied by the given multiplier, reconverted to bytes and written in our mutable byte array. The edited file is output to the designated folder inside of Game Files.

Creating all instances of the Enemy class:
I wrote the " _pars.py" files to generate the code for all the instances of the Enemy class, which I copied from the terminal and pasted into the " _clas.py" files. 

This is where the JSON files are used. The JSON files are created from a Serializer from this project: https://github.com/ithinkandicode/bloodstained-tools/tree/master/Serializer

* There are some disparities between all the pars.py files. I'll detail what the output for everything should look like later but I'll give the basic idea of what they do.

The pars files start with a root directory that contains the path to the location with all the relevant json files (these were created beforehand with the serializer). The path of each JSON file is opened, and information is taken and assigned to a string. Each of these strings is printed to the console, which I copy pasted into the clas files. 

Example output:
_# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb11_CustomStatusTable.uexp'
Land_amber = Enemy(stshinjuCustomPath, 140)
Land_amber = Enemy(stshinjuCustomPath, 1764)
Land_amber = Enemy(stshinjuCustomPath, 3388)
Land_amber = Enemy(stshinjuCustomPath, 5012)
Land_amber = Enemy(stshinjuCustomPath, 6636)
Land_amber = Enemy(stshinjuCustomPath, 8260)
Land_amber = Enemy(stshinjuCustomPath, 9884)


I suppose now I should indicate what each clas file deals with and I'll layout what the final directory structure needs to look like so it can easily be repaked with the UnrealPak tool. 

ene_clas.py deals with common enemies, files in two different locations, the uexp files located in (using the game's directory structure that will be included in the finished pak file):
- 'Trials of Mana\Content\Game00\Data\Csv\CharaData\EnemyStatusTable.uexp',
- 'Trials of Mana\Content\Game00\Data\Csv\CharaData\EnemyStatusMaxTable.uexp',
and every file in the following directory that starts with either 'EnemyStatusSt' or 'EnemyCustomStatusTable' in:
- 'Trials of Mana\Content\Game00\BP\Enemy\Zako\Data'

boss_clas.py deals with bosses, located in:
- 'Trials of Mana\Content\Game00\Data\Csv\CharaData\BossStatusTable.uexp

shinju_pars_custom.py deals with boss limbs and adds, the directories and files found in:
- 'Trials of Mana\Content\Game00\Data\Csv\CharaData\ShinjuStatusTableList'
The game's directory structure (the way the files need to be layed out after editing and output) can be viewed by going to the repo's 'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList' directory.

** As I was writing this, I noticed that I may have missed a folder that holds more boss limbs and whatnot. I'll need to add them to the repo and run the serializer on them to get their JSON files. The file path for that folder is in:
- 'Trials of Mana\Content\Game00\Data\Csv\CharaData\Parts'

** A potential bug I just noticed: the custom class instances share the same variable name. Would this lead to the class instance overwriting itself, meaning all enemies except the last one will be skipped?

The final pak file is created with UnrealPak. I downloaded it from this mega link provided by the bloodstained modding discord: https://mega.nz/file/BY0gUIqI#rYaUGom59yFDLNGtwai1W_QSeLZDIEd3qFbeApJ5f3Q
This download also includes the above-mentioned Serializer.

An example of making a pak file if we use only the boss files, put the game's directory path, for example, 'Trials of Mana\Content\Game00\Data\Csv\CharaData\BossStatusTable.uexp'. Put all of that inside another folder, named what you want the pak file to be called. I used 'BossMod_P' for example. It needs to end with '_P' to work. Drag that folder onto 'UnrealPak-Without-Compression.bat'.

I'm sure I'm missed some details so please don't hesitate to pelt me with questions.
