import json

with open(r"Game Files\JSON for viewing\Orig\_GodEnemyCustomStatusTable.json", "r") as read_file:
    data = json.load(read_file)


def printVars(numberSuffix, path):    
    
    newPathVar = "st" + str(numberSuffix) + "Path"
    
    offsetIterator = 111

    toPrint = "# ****** EnemyStatusSt" + numberSuffix + " - *****" + "\n" + newPathVar + " = " + "r'" + path + "'" + '\n'

    # data is a list; entry here is a dict object (it's like each enemy, basically)
    for entry in data:        
        
        enemyName = entry['Value']['Name_29_7A62483740A6D0DF1414CB9963F7CF87']
        enemyHP = entry['Value']['Hp_2_D1FBB5E1450A631F5BB06780E7A9D1EF']

        # statName is each individual element for "Value": "Name_...", "HP_..." etc.
        # entry['Value'][statName] is the value of each statName: 'SAHAGIN' for "Name_..." etc.                   

        if enemyName == 'dummy':                
            offsetIterator += 1579
            continue
        
        # *** TEMPORARY COMMENT OUT TO LEAVE IN ENEMIES WITH 1 HP (custom table)
        # if enemyHP == 1:      
        #     offsetIterator += 1579
        #     continue

        toPrint += str(enemyName) + " = Enemy(" + newPathVar + ", " + str(offsetIterator) + ")" + '\n'
        offsetIterator += 1579                               
        
    print(toPrint)

    with open('custom_output.txt', 'w') as f:
        f.write(toPrint)

            
printVars('godstcustom', r'Game Files\uexp files\Orig\GodEnemyCustomStatusTable.uexp')
