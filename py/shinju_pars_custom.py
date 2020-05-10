# Use the bos_pars offsets for the shinjucustom files

import json
import os


def printVars(numberSuffix, path):    
    
    newPathVar = "st" + str(numberSuffix) + "Path"
    
    offsetIterator = 140

    toPrint = "# ****** EnemyStatusSt" + numberSuffix + " - *****" + "\n" + newPathVar + " = " + "r'" + path + "'" + '\n'

    # data is a list; entry here is a dict object (it's like each enemy, basically)
    for entry in data:        
        
        enemyName = entry['Value']['Name_29_7A62483740A6D0DF1414CB9963F7CF87']
        enemyHP = entry['Value']['Hp_2_D1FBB5E1450A631F5BB06780E7A9D1EF']

        # statName is each individual element for "Value": "Name_...", "HP_..." etc.
        # entry['Value'][statName] is the value of each statName: 'SAHAGIN' for "Name_..." etc.                   
        
        if enemyName == 'dummy':                
            offsetIterator += 1624
            continue
        
        # *** TEMPORARY COMMENT OUT TO LEAVE IN ENEMIES WITH 1 HP (custom table)
        # if enemyHP == 1:      
        #     offsetIterator += 1579
        #     continue

        # TODO *** format enemyName so that it prints as an acceptable python variable (replace spaces with '_', etc.)
        enemyName = enemyName.replace(" ", "_")
        enemyName = enemyName.replace("-", "")
        enemyName = enemyName.replace(":", "")
        enemyName = enemyName.replace("__", "_")

        toPrint += str(enemyName) + " = Enemy(" + newPathVar + ", " + str(offsetIterator) + ")" + '\n'
        offsetIterator += 1624                               
        
    print(toPrint)

    # # write to custom file
    # with open('shinju_output.txt', 'w') as f:
    #     f.write(toPrint)


# Start for file iterating
rootdir = r'Game Files\Boss\Orig\JSON for viewing\ShinjuStatusTableList'

varNamerIncrement = 0

# Get full path of file to use
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        fullPath = os.path.join(subdir, file)
        
        # # fullPath gives us the full path of every single file in rootdir
        # print(fullPath)

        # # file gives us the name of each json file (NOT the full path)
        # print(file)        

        with open(fullPath, 'r') as f:
            data = json.load(f)

        if fullPath.startswith('Game Files\\Boss\\Orig\\JSON for viewing\\ShinjuStatusTableList\\_e'):
            uexpStartingPath = 'Game Files\\Boss\\Orig\\uexp files\\ShinjuStatusTableList\\'
            numSuffixForFunc = 'shinjuCustom'
        elif fullPath.startswith('Game Files\\Boss\\Orig\\JSON for viewing\\ShinjuStatusTableList\\eb'):
            # slice only the unique folder into a string
            uniqueFolder = fullPath[60:70]
            uexpStartingPath = 'Game Files\\Boss\\Orig\\uexp files\\ShinjuStatusTableList\\' + uniqueFolder + "\\"
            numSuffixForFunc = uniqueFolder + str(varNamerIncrement)
            # increment a variable to give each one a unique var name
            varNamerIncrement += 1
            
        # make variable for path to uexp
        newUexpFileName = file[1:]
        newUexpFileName = newUexpFileName.replace("json", "uexp")
        uexpPath = uexpStartingPath + newUexpFileName
        
        printVars(numSuffixForFunc, uexpPath)

