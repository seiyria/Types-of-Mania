# Trials-of-Mania---Difficulty-Mod
This mod aims to offer players a more challenging experience in Trials of Mana by making enemies more of a threat and harder to take down. All enemy stats are increased by a specified amount.

Apologies in advance for incorrect terminology.

The "Game Files" directory holds both the input and output files for the scripts. The "Boss" subdirectory contains the files used by "bos_clas.py", "bos_parse.py", "shinju_clas.py", and "shinju_pars.py". The other two, "JSON for viewing" and "uexp files" subdirs hold the files used by "ene_clas.py" and "ene_pars.py".

The " _clas.py" files aim to create an Enemy object that will hold offset locations for each stat of each Enemy instance that is created.
These offset locations point the editHexAll function to the index at which it will make edits to byte data in whatever 'uexp' file it is currently working with. Each instance is added to the 'enemyInstList' array which is looped through in the editHexAll function.

editHexAll function:
It grabs the full pathname of each file from 'rootdir', reads it as byte data, which is then assigned to 'mutableBytes' as a mutable bytearray. Each element (enemy) in 'enemyInstList' is iterated through and each offset attribute is used to grab the four bytes we need to edit. Those four bytes are converted to an integer, multiplied by the given multiplier, reconverted to bytes and written in our mutable byte array. The edited file is output to the designated folder inside of Game Files.

Creating all instances of the Enemy class:
I wrote the " _pars.py" files to generate the code for all the instances of the Enemy class, which I copied from the terminal and pasted into the " _clas.py" files. 

This is where the JSON files are used. The JSON files are created from a Serializer from this project: https://github.com/ithinkandicode/bloodstained-tools/tree/master/Serializer

