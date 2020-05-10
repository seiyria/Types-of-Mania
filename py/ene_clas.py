import os
import time


# Global list for iterating through and making edits to .uexp files
enemyInstList = []
bossInstList = []
shinjuInstList = []
partsInstList = []

# paths we want the edited files to output to for UnrealPak.exe
finDirPath_BP = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\BP\\Enemy\\Zako\\Data\\'
finDirPath_Data = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\'
finDirPath_Boss = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\'
finDirPath_shinju = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\ShinjuStatusTableList\\'
finDirPath_parts = 'Custom_TofMania - 0.3_P\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\Parts\\'


# TODO do we want to be able to update each class instance so we can check what its new value is?
class Enemy:    
    def __init__(self, file_path, hpOffset):
        self.fileLocation = file_path
        
        self.attrOffsetDict = {}                
        
        # Append to global list for iterating
        enemyInstList.append(self)

        # Offset locations for each stat we want to edit      
        # hpOffset is used as the base offset to calculate the other offsets  
        self.attrOffsetDict['hp'] = hpOffset
        self.attrOffsetDict['atk'] = hpOffset + (29 * 3)
        self.attrOffsetDict['def'] = hpOffset + (29 * 4)
        self.attrOffsetDict['agi'] = hpOffset + (29 * 5)
        self.attrOffsetDict['int'] = hpOffset + (29 * 6)
        self.attrOffsetDict['spr'] = hpOffset + (29 * 7)
        self.attrOffsetDict['luck'] = hpOffset + (29 * 8)
        self.attrOffsetDict['defMag'] = hpOffset + (29 * 9)
        self.attrOffsetDict['offMag'] = hpOffset + (29 * 10)
        self.attrOffsetDict['exp'] = hpOffset + (822)
    
    # TODO method to see current attr values
    def seeInfo(self):
        print("HP value: ")


class Boss:
    # hpOffset is used as the base offset to calculate the other offsets
    def __init__(self, file_path, hpOffset):
        self.fileLocation = file_path
        
        self.attrOffsetDict = {}                
        
        # Append to global list for iterating
        bossInstList.append(self)

        # Offset locations for each stat we want to edit        
        self.attrOffsetDict['hp'] = hpOffset
        self.attrOffsetDict['atk'] = hpOffset + (29 * 3)
        self.attrOffsetDict['def'] = hpOffset + (29 * 4)
        self.attrOffsetDict['agi'] = hpOffset + (29 * 5)
        self.attrOffsetDict['int'] = hpOffset + (29 * 6)
        self.attrOffsetDict['spr'] = hpOffset + (29 * 7)
        self.attrOffsetDict['luck'] = hpOffset + (29 * 8)
        self.attrOffsetDict['defMag'] = hpOffset + (29 * 9)
        self.attrOffsetDict['offMag'] = hpOffset + (29 * 10)
        self.attrOffsetDict['exp'] = hpOffset + (822)
    
    # TODO method to see current attr values
    def seeInfo(self):
        print("HP value: ")


class Shinju:
    # hpOffset is used as the base offset to calculate the other offsets
    def __init__(self, file_path, hpOffset):
        self.fileLocation = file_path
        
        self.attrOffsetDict = {}                
        
        # Append to global list for iterating
        shinjuInstList.append(self)

        # Offset locations for each stat we want to edit
        # self.hpOffset = hpOffset
        self.attrOffsetDict['hp'] = hpOffset
        self.attrOffsetDict['atk'] = hpOffset + (29 * 3)
        self.attrOffsetDict['def'] = hpOffset + (29 * 4)
        self.attrOffsetDict['agi'] = hpOffset + (29 * 5)
        self.attrOffsetDict['int'] = hpOffset + (29 * 6)
        self.attrOffsetDict['spr'] = hpOffset + (29 * 7)
        self.attrOffsetDict['luck'] = hpOffset + (29 * 8)
        self.attrOffsetDict['defMag'] = hpOffset + (29 * 9)
        self.attrOffsetDict['offMag'] = hpOffset + (29 * 10)
        self.attrOffsetDict['exp'] = hpOffset + (822)
    
    # TODO method to see current attr values
    def seeInfo(self):
        print("HP value: ")

class Parts:
    # hpOffset is used as the base offset to calculate the other offsets
    def __init__(self, file_path, hpOffset):
        self.fileLocation = file_path
        
        self.attrOffsetDict = {}                
        
        # Append to global list for iterating
        partsInstList.append(self)

        # Offset locations for each stat we want to edit
        # self.hpOffset = hpOffset
        self.attrOffsetDict['hp'] = hpOffset
        self.attrOffsetDict['atk'] = hpOffset + (29 * 3)
        self.attrOffsetDict['def'] = hpOffset + (29 * 4)
        self.attrOffsetDict['agi'] = hpOffset + (29 * 5)
        self.attrOffsetDict['int'] = hpOffset + (29 * 6)
        self.attrOffsetDict['spr'] = hpOffset + (29 * 7)
        self.attrOffsetDict['luck'] = hpOffset + (29 * 8)
        self.attrOffsetDict['defMag'] = hpOffset + (29 * 9)
        self.attrOffsetDict['offMag'] = hpOffset + (29 * 10)
        self.attrOffsetDict['exp'] = hpOffset + (822)
    
    # TODO method to see current attr values
    def seeInfo(self):
        print("HP value: ")


# TODO add an if statement to skip enemies with a value of 1 HP and adjust offset accordingly
# TODO add a conditional check to skip code if argument value (param?) is 0
def editHexAll(multiDict):
    
    # Start for file iterating
    rootdir = r'Game Files\uexp files\Orig'

    # Get full path of file to use
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # This will concatenate the 'head' and 'tail' to form the full file path
            fullPath = os.path.join(subdir, file)
            
            with open(fullPath, 'rb') as f:
                byteData = f.read()
        
            # Get data into an array that is mutable
            mutableBytes = bytearray(byteData)

            for enemy in enemyInstList:                
                # Check each Enemy's fileLocation attr to see if it matches the current fullPath
                if enemy.fileLocation == fullPath:
                    for attr, offset in enemy.attrOffsetDict.items():
                        
                        # Original slice of four bytes in data that we will edit
                        fourBytesToEdit = byteData[offset:(offset + 4)]                    

                        # Convert those four bytes to an integer
                        numFromBytes = int.from_bytes(fourBytesToEdit, byteorder='little', signed=True)                    

                        newStatValue = round(numFromBytes * multiDict[attr])
                        
                        if newStatValue > 2147483647:
                            newStatValue = 2147483647                 

                        # new Stat value to 4 byte string
                        bytesToInsert = newStatValue.to_bytes(4, byteorder='little', signed=True)                    

                        # Insert new byte slice into mutable byte array
                        mutableBytes[offset:(offset + 4)] = bytesToInsert                    

            # TODO Do we need to find a way to make the directories if they don't exist?
            # We'll simply change the output to where we want it in the folder to be used by UnrealPak
            # Write current file and output
            # TODO if check to see where the file needs to go
            if file == 'EnemyStatusTable.uexp' or file == 'EnemyStatusMaxTable.uexp':
                outPath = finDirPath_Data + file
                # TODO create nonexisting directory
                if not os.path.exists(finDirPath_Data):
                    os.makedirs(finDirPath_Data)
            else:
                outPath = finDirPath_BP + file
                if not os.path.exists(finDirPath_BP):
                    os.makedirs(finDirPath_BP)
            
            # TODO I think this could potentially write out the BossStatusTable.uexp file, we don't want that
            with open(outPath, 'wb') as f:
                f.write(mutableBytes)                    


def editHexAll_Boss(bossDict):
    
    # Start for file iterating
    rootdir = r'Game Files\Boss\Orig\uexp files'

    # Get full path of file to use
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fullPath = os.path.join(subdir, file)
            
            with open(fullPath, 'rb') as f:
                byteData = f.read()
        
            # Get data into an array that is mutable
            mutableBytes = bytearray(byteData)

            for boss in bossInstList:                
                # Check each Boss's fileLocation attr to see if it matches the current fullPath
                if boss.fileLocation == fullPath:
                    for attr, offset in boss.attrOffsetDict.items():
                        
                        # Original slice of four bytes in data that we will edit
                        fourBytesToEdit = byteData[offset:(offset + 4)]                    

                        # Convert those four bytes to an integer
                        numFromBytes = int.from_bytes(fourBytesToEdit, byteorder='little', signed=True)                    

                        newStatValue = round(numFromBytes * bossDict[attr])
                        # I don't think 99999 is the highest value allowed, so can maybe change in the future
                        if newStatValue > 2147483647:
                            newStatValue = 2147483647           

                        # new Stat value to 4 byte string
                        bytesToInsert = newStatValue.to_bytes(4, byteorder='little', signed=True)                    

                        # Insert new byte slice into mutable byte array
                        arrayToEdit = mutableBytes[offset:(offset + 4)]
                        mutableBytes[offset:(offset + 4)] = bytesToInsert  

                        # checkMe = mutableBytes[offset:(offset + 4)]     
                        # print(checkMe)
                        # print(mutableBytes[0:10])


            if file == 'BossStatusTable.uexp':
                outPath = finDirPath_Boss + file
                # TODO create nonexisting directory
                if not os.path.exists(finDirPath_Boss):
                    os.makedirs(finDirPath_Boss)            
                with open(outPath, 'wb') as f:
                    f.write(mutableBytes)
            else:
                continue


def editHexAll_Shinju(shinjuDict):
    
    # Start for file iterating
    rootdir = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList'

    # Get full path of file to use
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fullPath = os.path.join(subdir, file)
            
            with open(fullPath, 'rb') as f:
                byteData = f.read()
        
            # Get data into an array that is mutable
            mutableBytes = bytearray(byteData)

            for enemy in shinjuInstList:                
                # Check each Shinju's fileLocation attr to see if it matches the current fullPath
                if enemy.fileLocation == fullPath:
                    for attr, offset in enemy.attrOffsetDict.items():
                        
                        # Original slice of four bytes in data that we will edit
                        fourBytesToEdit = byteData[offset:(offset + 4)]                    

                        # Convert those four bytes to an integer
                        numFromBytes = int.from_bytes(fourBytesToEdit, byteorder='little', signed=True)                    

                        newStatValue = round(numFromBytes * shinjuDict[attr])
                        # I don't think 99999 is the highest value allowed, so can maybe change in the future
                        if newStatValue > 2147483647:
                            newStatValue = 2147483647           

                        # new Stat value to 4 byte string
                        bytesToInsert = newStatValue.to_bytes(4, byteorder='little', signed=True)                    

                        # Insert new byte slice into mutable byte array
                        mutableBytes[offset:(offset + 4)] = bytesToInsert                    


            if 'CustomStatusTable.uexp' in file:
                outPath = finDirPath_shinju + file
                # TODO create nonexisting directory
                if not os.path.exists(finDirPath_shinju):
                    os.makedirs(finDirPath_shinju)
            elif '_eb11_' in file:                
                newPath11 = finDirPath_shinju + "eb11_Parts"
                if not os.path.exists(newPath11):
                    os.makedirs(newPath11)
                    outPath = newPath11 + "\\" + file
                else:
                    outPath = newPath11 + "\\" + file
            elif '_eb12_' in file:                
                newPath12 = finDirPath_shinju + "eb12_Parts"
                if not os.path.exists(newPath12):
                    os.makedirs(newPath12)
                    outPath = newPath12 + "\\" + file
                else:
                    outPath = newPath12 + "\\" + file
            elif '_eb13_' in file:                
                newPath13 = finDirPath_shinju + "eb13_Parts"
                if not os.path.exists(newPath13):
                    os.makedirs(newPath13)
                    outPath = newPath13 + "\\" + file
                else:
                    outPath = newPath13 + "\\" + file
            elif '_eb14_' in file:                
                newPath14 = finDirPath_shinju + "eb14_Parts"
                if not os.path.exists(newPath14):
                    os.makedirs(newPath14)
                    outPath = newPath14 + "\\" + file
                else:
                    outPath = newPath14 + "\\" + file  
            elif '_eb15_' in file:                
                newPath15 = finDirPath_shinju + "eb15_Parts"
                if not os.path.exists(newPath15):
                    os.makedirs(newPath15)
                    outPath = newPath15 + "\\" + file
                else:
                    outPath = newPath15 + "\\" + file
            elif '_eb16_' in file:                
                newPath16 = finDirPath_shinju + "eb16_Parts"
                if not os.path.exists(newPath16):
                    os.makedirs(newPath16)
                    outPath = newPath16 + "\\" + file
                else:
                    outPath = newPath16 + "\\" + file
            elif '_eb17_' in file:                
                newPath17 = finDirPath_shinju + "eb17_Parts"
                if not os.path.exists(newPath17):
                    os.makedirs(newPath17)
                    outPath = newPath17 + "\\" + file
                else:
                    outPath = newPath17 + "\\" + file              
            else:
                continue

            # Write files
            with open(outPath, 'wb') as f:
                f.write(mutableBytes)


def editHexAll_Parts(partsDict):
    
    # Start for file iterating    
    rootdir = r'Game Files\Boss\Orig\uexp files\Parts'

    # Get full path of file to use
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # This will concatenate the 'head' and 'tail' to form the full file path
            fullPath = os.path.join(subdir, file)
            
            with open(fullPath, 'rb') as f:
                byteData = f.read()
        
            # Get data into an array that is mutable
            mutableBytes = bytearray(byteData)

            for enemy in partsInstList:                
                # Check each Enemy's fileLocation attr to see if it matches the current fullPath
                if enemy.fileLocation == fullPath:
                    for attr, offset in enemy.attrOffsetDict.items():
                        
                        # Original slice of four bytes in data that we will edit
                        fourBytesToEdit = byteData[offset:(offset + 4)]                    

                        # Convert those four bytes to an integer
                        numFromBytes = int.from_bytes(fourBytesToEdit, byteorder='little', signed=True)                    

                        newStatValue = round(numFromBytes * multiDict[attr])
                        
                        if newStatValue > 2147483647:
                            newStatValue = 2147483647                 

                        # new Stat value to 4 byte string
                        bytesToInsert = newStatValue.to_bytes(4, byteorder='little', signed=True)                    

                        # Insert new byte slice into mutable byte array
                        mutableBytes[offset:(offset + 4)] = bytesToInsert                    
            
            # We'll simply change the output to where we want it in the folder to be used by UnrealPak
            # Write current file and output                    
            outPath = finDirPath_parts + file
            if not os.path.exists(finDirPath_parts):
                os.makedirs(finDirPath_parts)
                        
            with open(outPath, 'wb') as f:
                f.write(mutableBytes)


#region Enemy Instance Creation Start

# ****** EnemyStatusSt01_2 - *****

st1_2Path = r'Game Files\uexp files\Orig\EnemyStatusSt01_2.uexp'

BOUNDWOLF_Lv6 = Enemy(st1_2Path, 1690)


# ****** EnemyStatusSt02 - Rabite Forest*****

st2Path = r'Game Files\uexp files\Orig\EnemyStatusSt02.uexp'

RABI_Lv1 = Enemy(st2Path, 1690)
MAIKONIDO_Lv1 = Enemy(st2Path, 3269)
BOUNDWOLF_Lv1 = Enemy(st2Path, 4848)
ASSASSINBUG_Lv1 = Enemy(st2Path, 6427)
RABI_Lv3 = Enemy(st2Path, 8006)
MAIKONIDO_Lv3 = Enemy(st2Path, 9585)
ASSASSINBUG_Lv3 = Enemy(st2Path, 11164)
RABI_Lv14 = Enemy(st2Path, 12743)
RABIRION_Lv15 = Enemy(st2Path, 14322)
MAIKONIDO_Lv14 = Enemy(st2Path, 15901)
ASSASSINBUG_Lv14 = Enemy(st2Path, 17480)
SUMMON_RABI_Lv15 = Enemy(st2Path, 19059)


# ****** EnemyStatusSt03 - *****

st3Path = r'Game Files\uexp files\Orig\EnemyStatusSt03.uexp'

RABI_Lv4 = Enemy(st3Path, 1690)
MAIKONIDO_Lv4 = Enemy(st3Path, 3269)
BATTOM_Lv4 = Enemy(st3Path, 4848)
GOBLIN_Lv4_AXE = Enemy(st3Path, 6427)
RABI_Lv5 = Enemy(st3Path, 8006)
MAIKONIDO_Lv5 = Enemy(st3Path, 9585)
BATTOM_Lv5 = Enemy(st3Path, 11164)
GOBLIN_Lv5_ARMOR = Enemy(st3Path, 12743)
ZOMBIE_Lv5 = Enemy(st3Path, 14322)


# ****** EnemyStatusSt09 - *****  *** This is where I started using a script for creating the instances

st9Path = r'Game Files\uexp files\Orig\EnemyStatusSt09.uexp'

RABI_Lv8 = Enemy(st9Path, 1690)
BATTOM_Lv8 = Enemy(st9Path, 3269)
GOBLIN_Lv8 = Enemy(st9Path, 4848)
ASSASSINBUG_Lv8 = Enemy(st9Path, 6427)
PORON_Lv8 = Enemy(st9Path, 8006)
ZOMBIE_Lv8 = Enemy(st9Path, 9585)
PORON_Lv8_DART = Enemy(st9Path, 11164)


# ****** EnemyStatusSt10 - *****

st10Path = r'Game Files\uexp files\Orig\EnemyStatusSt10.uexp'

RABI_LV8 = Enemy(st10Path, 1690)
GOBLIN_LV8 = Enemy(st10Path, 3269)


# ****** EnemyStatusSt12 - *****

st12Path = r'Game Files\uexp files\Orig\EnemyStatusSt12.uexp'

GOBLIN_LV10 = Enemy(st12Path, 1690)
GOBLINLORD_LV10 = Enemy(st12Path, 3269)
MALLBEAR_LV10 = Enemy(st12Path, 4848)
BATTOM_LV10 = Enemy(st12Path, 6427)
SLIME_LV10 = Enemy(st12Path, 8006)
MAIKONIDO_LV10 = Enemy(st12Path, 9585)


# ****** EnemyStatusSt13 - *****

st13Path = r'Game Files\uexp files\Orig\EnemyStatusSt13.uexp'

RABI_Lv1 = Enemy(st13Path, 1690)
MAIKONIDO_Lv1 = Enemy(st13Path, 3269)
MALLBEAR_LV11 = Enemy(st13Path, 4848)
UNUSED_RABI_LV11 = Enemy(st13Path, 6427)
BATTOM_LV11 = Enemy(st13Path, 8006)
UNUSED_GOBLINLORD_LV11 = Enemy(st13Path, 9585)
ASSASSINBUG_LV11 = Enemy(st13Path, 11164)
UNUSED_GALBEE_LV11 = Enemy(st13Path, 12743)
MALLBEAR_LV12 = Enemy(st13Path, 14322)
GOBLINLORD_LV12 = Enemy(st13Path, 15901)
GALBEE_LV12 = Enemy(st13Path, 17480)
BATTOM_LV12 = Enemy(st13Path, 19059)
MALLBEAR_LV13 = Enemy(st13Path, 20638)
BATTOM_LV13 = Enemy(st13Path, 22217)
GALBEE_LV13 = Enemy(st13Path, 23796)
RABI_Lv13 = Enemy(st13Path, 25375)
ASSASSINBUG_LV13 = Enemy(st13Path, 26954)
GOBLINLORD_LV13 = Enemy(st13Path, 28533)
MALLBEAR_LV40 = Enemy(st13Path, 30112)
GOBLINLORD_LV40 = Enemy(st13Path, 31691)


# ****** EnemyStatusSt15 - *****

st15Path = r'Game Files\uexp files\Orig\EnemyStatusSt15.uexp'

UNICORNHEAD_LV13_arm = Enemy(st15Path, 1690)
MAGICIAN_LV13 = Enemy(st15Path, 3269)
MACHINEGOLEM_LV13 = Enemy(st15Path, 4848)
UNICORNHEAD_LV15_arm = Enemy(st15Path, 6427)
MAGICIAN_LV16 = Enemy(st15Path, 8006)
MACHINEGOLEM_LV15_arm = Enemy(st15Path, 9585)


# ****** EnemyStatusSt18 - *****

st18Path = r'Game Files\uexp files\Orig\EnemyStatusSt18.uexp'

# Removed a period from "Lv.15" for ZOMBIE that came from the JSON file
ZOMBIE_Lv15 = Enemy(st18Path, 1690)
NEEDLEBIRD_Lv14 = Enemy(st18Path, 3269)
LITTLEDEVIL_Lv14 = Enemy(st18Path, 4848)
HARPY_Lv14 = Enemy(st18Path, 6427)
ARMORNIGHT_Lv14 = Enemy(st18Path, 8006)
ARMORNIGHT_Lv14_A = Enemy(st18Path, 9585)
NEEDLEBIRD_Lv15 = Enemy(st18Path, 11164)
LITTLEDEVIL_Lv15 = Enemy(st18Path, 12743)
HARPY_Lv15 = Enemy(st18Path, 14322)
ARMORNIGHT_Lv15_A = Enemy(st18Path, 15901)
ARMORNIGHT_Lv16_A = Enemy(st18Path, 17480)


# ****** EnemyStatusSt21 - *****

st21Path = r'Game Files\uexp files\Orig\EnemyStatusSt21.uexp'

ZOMBIE_Lv16 = Enemy(st21Path, 1690)
NEEDLEBIRD_Lv16 = Enemy(st21Path, 3269)
LITTLEDEVIL_Lv16 = Enemy(st21Path, 4848)
HARPY_Lv16 = Enemy(st21Path, 6427)
ARMORNIGHT_Lv16 = Enemy(st21Path, 8006)
ARMORNIGHT_Lv17_ARMOR = Enemy(st21Path, 9585)


# ****** EnemyStatusSt22 - *****

st22Path = r'Game Files\uexp files\Orig\EnemyStatusSt22.uexp'

NINJA_Lv1 = Enemy(st22Path, 1690)
LITTLEDEVIL_Lv18 = Enemy(st22Path, 3269)
ARMORNIGHT_Lv18 = Enemy(st22Path, 4848)
ARMORNIGHT_Lv19_ARMOR = Enemy(st22Path, 6427)
NINJA_Lv18 = Enemy(st22Path, 8006)
NINJA_Lv19_OMITARMOR = Enemy(st22Path, 9585)
EVILSWORD_Lv18 = Enemy(st22Path, 11164)


# ****** EnemyStatusSt23 - *****

st23Path = r'Game Files\uexp files\Orig\EnemyStatusSt23.uexp'

ZOMBIE_Lv21 = Enemy(st23Path, 1690)
GHOUL_Lv23 = Enemy(st23Path, 3269)
SLIME_Lv21 = Enemy(st23Path, 4848)
LITTLEDEVIL_Lv21 = Enemy(st23Path, 6427)
SPECTRE_Lv21 = Enemy(st23Path, 8006)
OGREBOX_Lv21 = Enemy(st23Path, 9585)
ZOMBIE_Lv21_N = Enemy(st23Path, 11164)
GHOUL_Lv23_N = Enemy(st23Path, 12743)
SLIME_Lv21_N = Enemy(st23Path, 14322)
LITTLEDEVIL_Lv21_N = Enemy(st23Path, 15901)
SPECTRE_Lv21_N = Enemy(st23Path, 17480)


# ****** EnemyStatusSt24 - *****

st24Path = r'Game Files\uexp files\Orig\EnemyStatusSt24.uexp'

RABIRION_LV23 = Enemy(st24Path, 1690)
DARKPRIEST_LV23 = Enemy(st24Path, 3269)
COCKATRICE_LV23 = Enemy(st24Path, 4848)
GOBLINLORD_LV23 = Enemy(st24Path, 6427)
GALBEE_LV23 = Enemy(st24Path, 8006)
MAIKONIDO_LV23 = Enemy(st24Path, 9585)
MALLBEAR_LV23 = Enemy(st24Path, 11164)
COCKATBIRD_LV23 = Enemy(st24Path, 12743)
SUMMON_RABI_LV23 = Enemy(st24Path, 14322)


# ****** EnemyStatusSt26 - *****

st26Path = r'Game Files\uexp files\Orig\EnemyStatusSt26.uexp'

BATTOM_Lv25 = Enemy(st26Path, 1690)
GOBLINLORD_Lv25 = Enemy(st26Path, 3269)
DARKPRIEST_Lv25 = Enemy(st26Path, 4848)
GRELL_Lv25 = Enemy(st26Path, 6427)
PAKKUNOTAMA_Lv25 = Enemy(st26Path, 8006)
PAKKUNTOKAGE_Lv25 = Enemy(st26Path, 9585)
POT_Lv25 = Enemy(st26Path, 11164)
MAMAPOT_Lv25 = Enemy(st26Path, 12743)
OGREBOX_Lv25 = Enemy(st26Path, 14322)


# ****** EnemyStatusSt28 - *****

st28Path = r'Game Files\uexp files\Orig\EnemyStatusSt28.uexp'

RABI_Lv1 = Enemy(st28Path, 1690)
SAHAGIN_Lv1 = Enemy(st28Path, 3269)
WIZARD_Lv25 = Enemy(st28Path, 4848)
SAHAGIN_Lv25 = Enemy(st28Path, 6427)
POT_Lv25 = Enemy(st28Path, 8006)
MAMAPOT_Lv25 = Enemy(st28Path, 9585)
PAKKUNTOKAGE_Lv26 = Enemy(st28Path, 11164)
SEASERPENT_Lv26 = Enemy(st28Path, 12743)
WIZARD_Lv26 = Enemy(st28Path, 14322)
SAHAGIN_Lv26 = Enemy(st28Path, 15901)


# ****** EnemyStatusSt31 - *****

st31Path = r'Game Files\uexp files\Orig\EnemyStatusSt31.uexp'

BARETTE_LV29 = Enemy(st31Path, 1690)
GOLDBARETTE_LV30 = Enemy(st31Path, 3269)
COCKATRICE_LV29 = Enemy(st31Path, 4848)
DARKPRIEST_LV29 = Enemy(st31Path, 6427)
DUCKSOLDIER_LV29 = Enemy(st31Path, 8006)
BIRD_LV29 = Enemy(st31Path, 9585)
DUCKSOLDIER_LV30_ARMOR = Enemy(st31Path, 11164)


# ****** EnemyStatusSt33 - *****

st33Path = r'Game Files\uexp files\Orig\EnemyStatusSt33.uexp'

FIREDRAKE_LV29 = Enemy(st33Path, 1690)
DUCKGENERAL_LV29 = Enemy(st33Path, 3269)
NINJAMASTER_LV29 = Enemy(st33Path, 4848)
SWORDMASTER_LV29 = Enemy(st33Path, 6427)
DARKPRIEST_LV29 = Enemy(st33Path, 8006)
FIREDRAKE_LV43 = Enemy(st33Path, 9585)
DUCKGENERAL_LV43 = Enemy(st33Path, 11164)
NINJAMASTER_LV43 = Enemy(st33Path, 12743)
SWORDMASTER_LV43 = Enemy(st33Path, 14322)
DARKPRIEST_LV43 = Enemy(st33Path, 15901)


# ****** EnemyStatusSt35 - *****

st35Path = r'Game Files\uexp files\Orig\EnemyStatusSt35.uexp'

RABI_Lv1 = Enemy(st35Path, 1690)
BOUNDWOLF_Lv1 = Enemy(st35Path, 3269)
BOUNDWOLF_Lv31 = Enemy(st35Path, 4848)
WEREWOLF_Lv32 = Enemy(st35Path, 6427)
DARKBATTOM_Lv31 = Enemy(st35Path, 8006)
BLACKFANG_Lv32_OMITARMOR = Enemy(st35Path, 9585)
SPECTRE_Lv31 = Enemy(st35Path, 11164)
BOUNDWOLF_Lv30 = Enemy(st35Path, 12743)
WEREWOLF_Lv30 = Enemy(st35Path, 14322)
DARKBATTOM_Lv30 = Enemy(st35Path, 15901)
BLACKFANG_Lv30_OMITARMOR = Enemy(st35Path, 17480)
SPECTRE_Lv30 = Enemy(st35Path, 19059)


# ****** EnemyStatusSt37 - *****

st37Path = r'Game Files\uexp files\Orig\EnemyStatusSt37.uexp'

DARTHMATANGO_LV32 = Enemy(st37Path, 1690)
POROBINHOOD_LV32 = Enemy(st37Path, 3269)
ASSASSINBUG_LV32 = Enemy(st37Path, 4848)
LADYBEE_LV32 = Enemy(st37Path, 6427)
MEGACRAWLER_LV32 = Enemy(st37Path, 8006)
DARTHMATANGO_LV33 = Enemy(st37Path, 9585)
POROBINHOOD_LV33 = Enemy(st37Path, 11164)
ASSASSINBUG_LV33 = Enemy(st37Path, 12743)
LADYBEE_LV33 = Enemy(st37Path, 14322)
MEGACRAWLER_LV33 = Enemy(st37Path, 15901)


# ****** EnemyStatusSt40 - *****

st40Path = r'Game Files\uexp files\Orig\EnemyStatusSt40.uexp'

ARMORNIGHT_LV34 = Enemy(st40Path, 1690)
HARPY_LV34 = Enemy(st40Path, 3269)
NEEDLEBIRD_LV34 = Enemy(st40Path, 4848)
LITTLEDEVIL_LV34 = Enemy(st40Path, 6427)


# ****** EnemyStatusSt41 - *****

st41Path = r'Game Files\uexp files\Orig\EnemyStatusSt41.uexp'

KINGRABI_LV35 = Enemy(st41Path, 1690)
RABI_LV35 = Enemy(st41Path, 3269)
RABIRION_LV35 = Enemy(st41Path, 4848)
MACHINEGOLEM_LV36 = Enemy(st41Path, 6427)
WIZARD_LV36 = Enemy(st41Path, 8006)
DARKPRIEST_LV36 = Enemy(st41Path, 9585)
NINJAMASTER_LV36 = Enemy(st41Path, 11164)
BLACKFANG_LV36 = Enemy(st41Path, 12743)
BOUNDWOLF_LV36 = Enemy(st41Path, 14322)
KINGRABI_LV36 = Enemy(st41Path, 15901)
RABI_LV36 = Enemy(st41Path, 17480)
RABIRION_LV36 = Enemy(st41Path, 19059)
SUMMON_RABI_LV36 = Enemy(st41Path, 20638)


# ****** EnemyStatusSt43 - *****

st43Path = r'Game Files\uexp files\Orig\EnemyStatusSt43.uexp'

UNICORNHEAD_Lv37 = Enemy(st43Path, 1690)
MAGICIAN_Lv37 = Enemy(st43Path, 3269)
WIZARD_Lv38 = Enemy(st43Path, 4848)
MACHINEGOLEM_Lv37 = Enemy(st43Path, 6427)
WIZARD_Lv39_OMITARMOR = Enemy(st43Path, 8006)
MACHINEGOLEM_Lv40 = Enemy(st43Path, 9585)


# ****** EnemyStatusSt44 - *****

st44Path = r'Game Files\uexp files\Orig\EnemyStatusSt44.uexp'

BOUNDWOLF_LV37 = Enemy(st44Path, 1690)
WEREWOLF_LV37 = Enemy(st44Path, 3269)
BLACKFANG_LV37 = Enemy(st44Path, 4848)
SILVERWOLF_LV37 = Enemy(st44Path, 6427)


# ****** EnemyStatusSt45 - *****

st45Path = r'Game Files\uexp files\Orig\EnemyStatusSt45.uexp'

NINJA_LV1 = Enemy(st45Path, 1690)
NINJA_LV37 = Enemy(st45Path, 3269)
NINJAMASTER_LV37 = Enemy(st45Path, 4848)
DARKPRIEST_LV37 = Enemy(st45Path, 6427)
LESSERDAEMON_LV37 = Enemy(st45Path, 8006)
NINJAMASTER_LV38 = Enemy(st45Path, 9585)


# ****** EnemyStatusSt47 - *****

st47Path = r'Game Files\uexp files\Orig\EnemyStatusSt47.uexp'

GIGACRAWLER_LV47 = Enemy(st47Path, 1690)
QUEENBEE_LV47 = Enemy(st47Path, 3269)
DARTHMATANGO_LV47 = Enemy(st47Path, 4848)
POROBINLEADER_LV47 = Enemy(st47Path, 6427)


# ****** EnemyStatusSt51 - *****

st51Path = r'Game Files\uexp files\Orig\EnemyStatusSt51.uexp'

BASILISK_LV53 = Enemy(st51Path, 1690)
PETITIAMATT_LV53 = Enemy(st51Path, 3269)
BOULDER_LV53 = Enemy(st51Path, 4848)
GUARDIAN_LV53 = Enemy(st51Path, 6427)
RASTERBUG_LV53 = Enemy(st51Path, 8006)
GREMLINS_LV53 = Enemy(st51Path, 9585)
LESSERDAEMON_LV53 = Enemy(st51Path, 11164)
KNIGHTBLADE_LV53 = Enemy(st51Path, 12743)
COCKATRICE_SUMMON_LV53 = Enemy(st51Path, 14322)
COCKATBIRD_SUMMON_LV53 = Enemy(st51Path, 15901)
BASILISK_LV54 = Enemy(st51Path, 17480)
PETITIAMATT_LV54 = Enemy(st51Path, 19059)
BOULDER_LV54 = Enemy(st51Path, 20638)
GUARDIAN_LV54 = Enemy(st51Path, 22217)
RASTERBUG_LV54 = Enemy(st51Path, 23796)
GREMLINS_LV54 = Enemy(st51Path, 25375)
LESSERDAEMON_LV54 = Enemy(st51Path, 26954)
KNIGHTBLADE_LV54 = Enemy(st51Path, 28533)
COCKATRICE_SUMMON_LV54 = Enemy(st51Path, 30112)
COCKATBIRD_SUMMON_LV54 = Enemy(st51Path, 31691)
GUARDIAN_LONG_LV53 = Enemy(st51Path, 33270)
GREMLINS_LONG_LV53 = Enemy(st51Path, 34849)
KNIGHTBLADE_LONG_LV53 = Enemy(st51Path, 36428)
LESSERDAEMON_LONG_LV53 = Enemy(st51Path, 38007)
RASTERBUG_LONG_LV53 = Enemy(st51Path, 39586)
GUARDIAN_LONG_LV54 = Enemy(st51Path, 41165)
GREMLINS_LONG_LV54 = Enemy(st51Path, 42744)
KNIGHTBLADE_LONG_LV54 = Enemy(st51Path, 44323)
LESSERDAEMON_LONG_LV54 = Enemy(st51Path, 45902)
RASTERBUG_LONG_LV54 = Enemy(st51Path, 47481)
PETITIAMATT_ARMOR_LV54 = Enemy(st51Path, 49060)
LESSERDAEMON_ARMOR_LV54 = Enemy(st51Path, 50639)
LESSERDAEMON_ARMOR_LONG_LV54 = Enemy(st51Path, 52218)


# ****** EnemyStatusSt52 - *****

st52Path = r'Game Files\uexp files\Orig\EnemyStatusSt52.uexp'

HIGHWIZARD_Lv55 = Enemy(st52Path, 1690)
DEATHMACHINE_Lv55 = Enemy(st52Path, 3269)
DARKLORD_Lv55 = Enemy(st52Path, 4848)
PAPAPOT_Lv55 = Enemy(st52Path, 6427)
PETITDRAGON_Lv55 = Enemy(st52Path, 8006)
FROSTDRAGON_Lv55 = Enemy(st52Path, 9585)
PETITIAMATT_Lv55 = Enemy(st52Path, 11164)
POWERBOULDER_Lv55 = Enemy(st52Path, 12743)
HIGHWIZARD_Lv56 = Enemy(st52Path, 14322)
DEATHMACHINE_Lv56 = Enemy(st52Path, 15901)
DARKLORD_Lv56 = Enemy(st52Path, 17480)
PAPAPOT_Lv56 = Enemy(st52Path, 19059)
HIGHWIZARD_Lv58 = Enemy(st52Path, 20638)
DEATHMACHINE_Lv58 = Enemy(st52Path, 22217)
PETITDRAGON_Lv58 = Enemy(st52Path, 23796)
FROSTDRAGON_Lv58 = Enemy(st52Path, 25375)
PETITIAMATT_Lv58 = Enemy(st52Path, 26954)
PETIDRAZOMBIE_Lv58 = Enemy(st52Path, 28533)
POWERBOULDER_Lv58 = Enemy(st52Path, 30112)
GREATDAEMON_Lv58 = Enemy(st52Path, 31691)
KAISERMIMIC_Lv58 = Enemy(st52Path, 33270)
HIGHWIZARD_Lv59 = Enemy(st52Path, 34849)
DEATHMACHINE_Lv59 = Enemy(st52Path, 36428)
PETITDRAGON_Lv59 = Enemy(st52Path, 38007)
FROSTDRAGON_Lv59 = Enemy(st52Path, 39586)
PETITIAMATT_Lv59 = Enemy(st52Path, 41165)
GREATDAEMON_Lv59 = Enemy(st52Path, 42744)
HIGHWIZARD_Lv60 = Enemy(st52Path, 44323)
DEATHMACHINE_Lv60 = Enemy(st52Path, 45902)
DARKLORD_Lv60 = Enemy(st52Path, 47481)
PAPAPOT_Lv60 = Enemy(st52Path, 49060)
PETITDRAGON_Lv60 = Enemy(st52Path, 50639)
FROSTDRAGON_Lv60 = Enemy(st52Path, 52218)
PETITIAMATT_Lv60 = Enemy(st52Path, 53797)
PETIDRAZOMBIE_Lv60 = Enemy(st52Path, 55376)
POWERBOULDER_Lv60 = Enemy(st52Path, 56955)
GREATDAEMON_Lv60 = Enemy(st52Path, 58534)
PETIDRAZOMBIE_Lv61 = Enemy(st52Path, 60113)
GREATDAEMON_Lv61 = Enemy(st52Path, 61692)
PETIDRAZOMBIE_ARMOR_Lv61 = Enemy(st52Path, 63271)
GREATDAEMON_ARMOR_Lv61 = Enemy(st52Path, 64850)


# ****** EnemyStatusSt53 - *****

st53Path = r'Game Files\uexp files\Orig\EnemyStatusSt53.uexp'

GREATRABI_Lv53 = Enemy(st53Path, 1690)
RASTERBUG_Lv53 = Enemy(st53Path, 3269)
UNICORNHEAD_Lv53 = Enemy(st53Path, 4848)
MAGICIAN_Lv53 = Enemy(st53Path, 6427)
GUARDIAN_Lv53 = Enemy(st53Path, 8006)
ARMORNIGHT_Lv53 = Enemy(st53Path, 9585)
NINJA_Lv53 = Enemy(st53Path, 11164)
EVILSWORD_Lv53 = Enemy(st53Path, 12743)
EVILSHERMAN_Lv53 = Enemy(st53Path, 14322)
PAPAPOT_Lv53 = Enemy(st53Path, 15901)
WOLFDEVIL_Lv53 = Enemy(st53Path, 17480)
BOULDER_Lv53 = Enemy(st53Path, 19059)
LESSERDAEMON_Lv53 = Enemy(st53Path, 20638)
GREATDAEMON_SUMMON_Lv53 = Enemy(st53Path, 22217)
LITTLEDEVIL_SUMMON_Lv53 = Enemy(st53Path, 23796)
GREMLINS_SUMMON_Lv53 = Enemy(st53Path, 25375)


# ****** EnemyStatusSt54 - *****

st54Path = r'Game Files\uexp files\Orig\EnemyStatusSt54.uexp'

DEATHMACHINE_LV56 = Enemy(st54Path, 1690)
ELEMENTSWORD_LV56 = Enemy(st54Path, 3269)
DARKPRIEST_LV56 = Enemy(st54Path, 4848)
GHOST_LV56 = Enemy(st54Path, 6427)
NECROMANCER_LV56 = Enemy(st54Path, 8006)
PETIDRAZOMBIE_LV56 = Enemy(st54Path, 9585)
CARMILLAQUEEN_Lv56 = Enemy(st54Path, 11164)
POWERBOULDER_Lv56 = Enemy(st54Path, 12743)
GREATDAEMON_Lv56 = Enemy(st54Path, 14322)
DEATHMACHINE_LV58 = Enemy(st54Path, 15901)
ELEMENTSWORD_LV58 = Enemy(st54Path, 17480)
NECROMANCER_LV58 = Enemy(st54Path, 19059)
PETIDRAZOMBIE_LV58 = Enemy(st54Path, 20638)
CARMILLAQUEEN_Lv58_OMITARMOR = Enemy(st54Path, 22217)
POWERBOULDER_Lv58 = Enemy(st54Path, 23796)
GREATDAEMON_Lv58_ARMOR = Enemy(st54Path, 25375)
UNICORNHEAD_LV56 = Enemy(st54Path, 26954)
BOUNDWOLF_LV56 = Enemy(st54Path, 28533)
ZOMBIE_LV56 = Enemy(st54Path, 30112)
GHOUL_LV57 = Enemy(st54Path, 31691)
SPECTRE_LV56 = Enemy(st54Path, 33270)
GHOST_LV58 = Enemy(st54Path, 34849)
ASSASSINBUG_LV56 = Enemy(st54Path, 36428)
POROBINHOOD_LV56 = Enemy(st54Path, 38007)
LADYBEE_LV56 = Enemy(st54Path, 39586)
MEGACRAWLER_LV56 = Enemy(st54Path, 41165)
LITTLEDEVIL_LV56 = Enemy(st54Path, 42744)
ARMORNIGHT_LV56 = Enemy(st54Path, 44323)
NINJA_LV56 = Enemy(st54Path, 45902)
EVILSWORD_LV56 = Enemy(st54Path, 47481)
SILVERWOLF_LV56 = Enemy(st54Path, 49060)
BLOODYWOLF_LV57 = Enemy(st54Path, 50639)
CARMILLA_LV56 = Enemy(st54Path, 52218)
BATTOM_LV56 = Enemy(st54Path, 53797)
GOBLINLORD_LV56 = Enemy(st54Path, 55376)
GRELL_LV56 = Enemy(st54Path, 56955)
KAISERMIMIC_Lv58 = Enemy(st54Path, 58534)
SUMMON_ZOMBIE_LV56 = Enemy(st54Path, 60113)
SUMMON_GHOUL_LV56 = Enemy(st54Path, 61692)
SUMMON_GHOST_LV56 = Enemy(st54Path, 63271)
SUMMON_ZOMBIE_LV58 = Enemy(st54Path, 64850)
SUMMON_GHOUL_LV58 = Enemy(st54Path, 66429)
SUMMON_GHOST_LV58 = Enemy(st54Path, 68008)


# ****** EnemyStatusSt55 - *****

st55Path = r'Game Files\uexp files\Orig\EnemyStatusSt55.uexp'

KERBEROS_Lv53 = Enemy(st55Path, 1690)
GREMLINS_Lv53 = Enemy(st55Path, 3269)
KNIGHTBLADE_Lv53 = Enemy(st55Path, 4848)
GHOST_Lv53 = Enemy(st55Path, 6427)
WOLFDEVIL_Lv53 = Enemy(st55Path, 8006)
PETITIAMATT_Lv53 = Enemy(st55Path, 9585)
BOULDER_Lv53 = Enemy(st55Path, 11164)
LESSERDAEMON_Lv53 = Enemy(st55Path, 12743)
KNIGHTBLADE_Lv55_OMITARMOR = Enemy(st55Path, 14322)
LESSERDAEMON_Lv55_ARMOR = Enemy(st55Path, 15901)


# ****** EnemyStatusSt56 - *****

st56Path = r'Game Files\uexp files\Orig\EnemyStatusSt56.uexp'

GOLDUNICO_Lv56 = Enemy(st56Path, 1690)
HIGHWIZARD_Lv56 = Enemy(st56Path, 3269)
DARKLORD_Lv56 = Enemy(st56Path, 4848)
ELEMENTSWORD_Lv56 = Enemy(st56Path, 6427)
EVILSHERMAN_Lv56 = Enemy(st56Path, 8006)
CARMILLAQUEEN_Lv56 = Enemy(st56Path, 9585)
POWERBOULDER_Lv56 = Enemy(st56Path, 11164)
GREATDAEMON_Lv56 = Enemy(st56Path, 12743)
KAISERMIMIC_Lv58 = Enemy(st56Path, 14322)
GOLDUNICO_Lv58_ARMOR = Enemy(st56Path, 15901)
DARKLORD_Lv58_ARMOR = Enemy(st56Path, 17480)
CARMILLAQUEEN_Lv58_OMITARMOR = Enemy(st56Path, 19059)
GREATDAEMON_Lv58_ARMOR = Enemy(st56Path, 20638)
SUMMON_LITTLEDEVIL_Lv56 = Enemy(st56Path, 22217)
SUMMON_GREMLINS_Lv56 = Enemy(st56Path, 23796)
SUMMON_GREATDAEMON_Lv56 = Enemy(st56Path, 25375)


# ****** EnemyStatusSt57 - *****

st57Path = r'Game Files\uexp files\Orig\EnemyStatusSt57.uexp'

SHAPESHIFTER_LV62 = Enemy(st57Path, 1690)
SHADOWZERO_LV63 = Enemy(st57Path, 3269)
SHAPESHIFTER_LV61 = Enemy(st57Path, 4848)


# ****** EnemyStatusSt67 - *****

st67Path = r'Game Files\uexp files\Orig\EnemyStatusSt67.uexp'

KERBEROS_Lv64 = Enemy(st67Path, 1690)
HIGHWIZARD_Lv64 = Enemy(st67Path, 3269)
DEATHMACHINE_Lv64 = Enemy(st67Path, 4848)
DARKLORD_Lv64 = Enemy(st67Path, 6427)
PETITIAMATT_Lv64 = Enemy(st67Path, 8006)
GREATDAEMON_Lv64 = Enemy(st67Path, 9585)


# ****** EnemyStatusSt67_A - *****

st67_APath = r'Game Files\uexp files\Orig\EnemyStatusSt67_A.uexp'

RASTERBUG_Lv64 = Enemy(st67_APath, 1690)
SLIMEPRINCE_Lv64 = Enemy(st67_APath, 3269)
NIDORION_Lv64 = Enemy(st67_APath, 4848)
QUEENBEE_Lv64 = Enemy(st67_APath, 6427)
BASILISK_Lv64 = Enemy(st67_APath, 8006)
GIGACRAWLER_Lv64 = Enemy(st67_APath, 9585)
COCKATRICE_SUMMON_Lv64 = Enemy(st67_APath, 11164)
COCKATBIRD_SUMMON_Lv64 = Enemy(st67_APath, 12743)


# ****** EnemyStatusSt67_B - *****

st67_BPath = r'Game Files\uexp files\Orig\EnemyStatusSt67_B.uexp'

WIZARD_Lv64 = Enemy(st67_BPath, 1690)
HIGHWIZARD_Lv64 = Enemy(st67_BPath, 3269)
SWORDNIGHT_Lv64 = Enemy(st67_BPath, 4848)
DARKLORD_Lv64 = Enemy(st67_BPath, 6427)
NINJAMASTER_Lv64 = Enemy(st67_BPath, 8006)
KNIGHTBLADE_Lv64 = Enemy(st67_BPath, 9585)
PETITDRAGON_Lv64 = Enemy(st67_BPath, 11164)
FROSTDRAGON_Lv64 = Enemy(st67_BPath, 12743)
PETITIAMATT_Lv64 = Enemy(st67_BPath, 14322)
PETIDRAZOMBIE_Lv64 = Enemy(st67_BPath, 15901)
KAISERMIMIC_Lv64 = Enemy(st67_BPath, 17480)


# ****** EnemyStatusSt67_C - *****

st67_CPath = r'Game Files\uexp files\Orig\EnemyStatusSt67_C.uexp'

COCKATRICE_Lv65 = Enemy(st67_CPath, 1690)
COCKABIRD_GROWTH_Lv65 = Enemy(st67_CPath, 3269)
GREMLINS_Lv65 = Enemy(st67_CPath, 4848)
NINJA_Lv65 = Enemy(st67_CPath, 6427)
NINJAMASTER_Lv65 = Enemy(st67_CPath, 8006)
KNIGHTBLADE_Lv65 = Enemy(st67_CPath, 9585)
EVILSHERMAN_Lv65 = Enemy(st67_CPath, 11164)
DUCKGENERAL_Lv65 = Enemy(st67_CPath, 12743)
GOLDBARETTE_Lv65 = Enemy(st67_CPath, 14322)
SHAPESHIFTER_Lv65 = Enemy(st67_CPath, 15901)
LITTLEDEVIL_SUMMON_Lv65 = Enemy(st67_CPath, 17480)
GREMLINS_SUMMON_Lv65 = Enemy(st67_CPath, 19059)
GREATDAEMON_SUMMON_Lv65 = Enemy(st67_CPath, 20638)


# ****** EnemyStatusSt67_E - *****

st67_EPath = r'Game Files\uexp files\Orig\EnemyStatusSt67_E.uexp'

ZOMBIE_Lv67 = Enemy(st67_EPath, 1690)
GHOUL_Lv67 = Enemy(st67_EPath, 3269)
SLIMEPRINCE_Lv67 = Enemy(st67_EPath, 4848)
GHOST_Lv67 = Enemy(st67_EPath, 6427)
NECROMANCER_Lv67 = Enemy(st67_EPath, 8006)
GRELLMAGE_Lv67 = Enemy(st67_EPath, 9585)
PAKKURIOTAMA_Lv67 = Enemy(st67_EPath, 11164)
PAKKUNDRAGON_Lv67 = Enemy(st67_EPath, 12743)
PETIDRAZOMBIE_Lv67 = Enemy(st67_EPath, 14322)
POWERBOULDER_Lv67 = Enemy(st67_EPath, 15901)
KAISERMIMIC_Lv67 = Enemy(st67_EPath, 17480)
ZOMBIE_Summon = Enemy(st67_EPath, 19059)
GHOUL_Summon = Enemy(st67_EPath, 20638)
GHOST_Summon = Enemy(st67_EPath, 22217)


# ****** EnemyStatusSt67_G - *****

st67_GPath = r'Game Files\uexp files\Orig\EnemyStatusSt67_G.uexp'

UNICORNHEAD_lv69 = Enemy(st67_GPath, 1690)
GOLDUNICO_lv69 = Enemy(st67_GPath, 3269)
HIGHWIZARD_lv69 = Enemy(st67_GPath, 4848)
GUARDIAN_lv69 = Enemy(st67_GPath, 6427)
DEATHMACHINE_lv69 = Enemy(st67_GPath, 8006)
PAPAPOT_lv69 = Enemy(st67_GPath, 9585)
SUMMON_SAHUAGIN_lv69 = Enemy(st67_GPath, 11164)
PETITPOSEIDON_lv69 = Enemy(st67_GPath, 12743)
SEADRAGON_lv69 = Enemy(st67_GPath, 14322)
FROSTDRAGON_LV69 = Enemy(st67_GPath, 15901)
SHADOWZERO_LV69 = Enemy(st67_GPath, 17480)
KAISERMIMIC = Enemy(st67_GPath, 19059)


# ****** EnemyStatusSt67_H - *****

st67_HPath = r'Game Files\uexp files\Orig\EnemyStatusSt67_H.uexp'

DARKBATTOM_lv69 = Enemy(st67_HPath, 1690)
BIRD_lv69 = Enemy(st67_HPath, 3269)
GREMLINS_lv69 = Enemy(st67_HPath, 4848)
SEIREN_lv69 = Enemy(st67_HPath, 6427)
ELEMENTSWORD_lv69 = Enemy(st67_HPath, 8006)
GIGACRAWLER_lv69 = Enemy(st67_HPath, 9585)
CARMILLAQUEEN_lv69 = Enemy(st67_HPath, 11164)
POWERBOULDER_lv69 = Enemy(st67_HPath, 12743)
LESSERDAEMON_lv69 = Enemy(st67_HPath, 14322)
GREATDAEMON_lv69 = Enemy(st67_HPath, 15901)
RABI_lv69 = Enemy(st67_HPath, 17480)
RABIRION_lv69 = Enemy(st67_HPath, 19059)
KINGRABI_lv69 = Enemy(st67_HPath, 20638)
GREATRABI_lv69 = Enemy(st67_HPath, 22217)
KAISERMIMIC_lv69 = Enemy(st67_HPath, 23796)
RABI_Summon = Enemy(st67_HPath, 25375)


# ****** EnemyStatusSt67_I - *****

st67_IPath = r'Game Files\uexp files\Orig\EnemyStatusSt67_I.uexp'

BEASTMASTER_lv71 = Enemy(st67_IPath, 1690)
KERBEROS_lv71 = Enemy(st67_IPath, 3269)
POROBINLEADER_lv71 = Enemy(st67_IPath, 4848)
FIREDRAKE_lv71 = Enemy(st67_IPath, 6427)
WEREWOLF_lv71 = Enemy(st67_IPath, 8006)
BLACKFANG_lv71 = Enemy(st67_IPath, 9585)
SILVERWOLF_lv71 = Enemy(st67_IPath, 11164)
BLOODYWOLF_lv71 = Enemy(st67_IPath, 12743)
WOLFDEVIL_lv71 = Enemy(st67_IPath, 14322)
GOLDBARETTE_Summon = Enemy(st67_IPath, 15901)
KERBEROS_Summon = Enemy(st67_IPath, 17480)


# ****** EnemyStatusStcustom - *****

stcustomPath = r'Game Files\uexp files\Orig\EnemyCustomStatusTable.uexp'

RABI_Lv1 = Enemy(stcustomPath, 1690)
RABI = Enemy(stcustomPath, 3269)
RABI = Enemy(stcustomPath, 4848)
RABI = Enemy(stcustomPath, 6427)
RABI_Lv3 = Enemy(stcustomPath, 9585)
RABI = Enemy(stcustomPath, 11164)
RABI = Enemy(stcustomPath, 12743)
RABI = Enemy(stcustomPath, 14322)
RABI = Enemy(stcustomPath, 15901)
RABI = Enemy(stcustomPath, 17480)
RABI = Enemy(stcustomPath, 19059)
RABI = Enemy(stcustomPath, 20638)
RABIRION = Enemy(stcustomPath, 22217)
RABIRION = Enemy(stcustomPath, 23796)
RABIRION = Enemy(stcustomPath, 25375)
KINGRABI = Enemy(stcustomPath, 26954)
GREATRABI = Enemy(stcustomPath, 28533)
MAIKONIDO = Enemy(stcustomPath, 30112)
MAIKONIDO = Enemy(stcustomPath, 31691)
MAIKONIDO = Enemy(stcustomPath, 33270)
MAIKONIDO = Enemy(stcustomPath, 34849)
MAIKONIDO = Enemy(stcustomPath, 36428)
MAIKONIDO = Enemy(stcustomPath, 38007)
MAIKONIDO = Enemy(stcustomPath, 39586)
DARTHMATANGO = Enemy(stcustomPath, 41165)
DARTHMATANGO = Enemy(stcustomPath, 53797)
BATTOM = Enemy(stcustomPath, 55376)
BATTOM = Enemy(stcustomPath, 56955)
BATTOM = Enemy(stcustomPath, 58534)
BATTOM = Enemy(stcustomPath, 60113)
BATTOM = Enemy(stcustomPath, 61692)
BATTOM = Enemy(stcustomPath, 63271)
BATTOM = Enemy(stcustomPath, 64850)
DARKBATTOM = Enemy(stcustomPath, 66429)
DARKBATTOM = Enemy(stcustomPath, 68008)
GOBLIN = Enemy(stcustomPath, 69587)
GOBLIN = Enemy(stcustomPath, 71166)
GOBLIN = Enemy(stcustomPath, 72745)
GOBLIN = Enemy(stcustomPath, 74324)
GOBLIN = Enemy(stcustomPath, 75903)
GOBLINLORD = Enemy(stcustomPath, 77482)
GOBLINLORD = Enemy(stcustomPath, 79061)
GOBLINLORD = Enemy(stcustomPath, 80640)
GOBLINLORD = Enemy(stcustomPath, 82219)
GOBLINLORD = Enemy(stcustomPath, 83798)
GOBLINLORD = Enemy(stcustomPath, 85377)
BEASTMASTER = Enemy(stcustomPath, 98009)
BEASTMASTER = Enemy(stcustomPath, 99588)
BOUNDWOLF = Enemy(stcustomPath, 101167)
BOUNDWOLF = Enemy(stcustomPath, 102746)
BOUNDWOLF = Enemy(stcustomPath, 104325)
BOUNDWOLF = Enemy(stcustomPath, 105904)
BOUNDWOLF = Enemy(stcustomPath, 107483)
BOUNDWOLF = Enemy(stcustomPath, 109062)
BOUNDWOLF = Enemy(stcustomPath, 110641)
KERBEROS = Enemy(stcustomPath, 123273)
KERBEROS = Enemy(stcustomPath, 124852)
ASSASSINBUG_Lv3 = Enemy(stcustomPath, 126431)
ASSASSINBUG = Enemy(stcustomPath, 128010)
ASSASSINBUG = Enemy(stcustomPath, 129589)
ASSASSINBUG = Enemy(stcustomPath, 131168)
ASSASSINBUG = Enemy(stcustomPath, 132747)
ASSASSINBUG = Enemy(stcustomPath, 134326)
RASTERBUG = Enemy(stcustomPath, 135905)
RASTERBUG = Enemy(stcustomPath, 137484)
PORON = Enemy(stcustomPath, 139063)
POROBINHOOD = Enemy(stcustomPath, 140642)
POROBINHOOD = Enemy(stcustomPath, 142221)
POROBINLEADER = Enemy(stcustomPath, 154853)
POROBINLEADER = Enemy(stcustomPath, 156432)
ZOMBIE = Enemy(stcustomPath, 159590)
ZOMBIE = Enemy(stcustomPath, 161169)
ZOMBIE = Enemy(stcustomPath, 162748)
ZOMBIE = Enemy(stcustomPath, 164327)
ZOMBIE = Enemy(stcustomPath, 165906)
ZOMBIE = Enemy(stcustomPath, 167485)
GHOUL = Enemy(stcustomPath, 169064)
GHOUL = Enemy(stcustomPath, 181696)
GHOUL = Enemy(stcustomPath, 183275)
SLIME = Enemy(stcustomPath, 184854)
SLIME = Enemy(stcustomPath, 186433)
SLIMEPRINCE = Enemy(stcustomPath, 199065)
MALLBEAR = Enemy(stcustomPath, 200644)
MALLBEAR = Enemy(stcustomPath, 202223)
MALLBEAR = Enemy(stcustomPath, 203802)
MALLBEAR = Enemy(stcustomPath, 205381)
NIDORION = Enemy(stcustomPath, 218013)
GALBEE = Enemy(stcustomPath, 219592)
GALBEE = Enemy(stcustomPath, 221171)
LADYBEE = Enemy(stcustomPath, 222750)
LADYBEE = Enemy(stcustomPath, 224329)
QUEENBEE = Enemy(stcustomPath, 236961)
UNICORNHEAD = Enemy(stcustomPath, 238540)
UNICORNHEAD = Enemy(stcustomPath, 240119)
UNICORNHEAD = Enemy(stcustomPath, 243277)
UNICORNHEAD = Enemy(stcustomPath, 244856)
GOLDUNICO = Enemy(stcustomPath, 246435)
GOLDUNICO = Enemy(stcustomPath, 248014)
MAGICIAN = Enemy(stcustomPath, 249593)
MAGICIAN = Enemy(stcustomPath, 251172)
WIZARD = Enemy(stcustomPath, 254330)
WIZARD = Enemy(stcustomPath, 255909)
WIZARD = Enemy(stcustomPath, 257488)
WIZARD = Enemy(stcustomPath, 259067)
HIGHWIZARD = Enemy(stcustomPath, 260646)
HIGHWIZARD = Enemy(stcustomPath, 262225)
HIGHWIZARD = Enemy(stcustomPath, 263804)
MACHINEGOLEM = Enemy(stcustomPath, 265383)
MACHINEGOLEM = Enemy(stcustomPath, 266962)
MACHINEGOLEM = Enemy(stcustomPath, 268541)
GUARDIAN = Enemy(stcustomPath, 270120)
GUARDIAN = Enemy(stcustomPath, 271699)
DEATHMACHINE = Enemy(stcustomPath, 273278)
DEATHMACHINE = Enemy(stcustomPath, 274857)
COCKATRICE = Enemy(stcustomPath, 276436)
COCKATRICE = Enemy(stcustomPath, 278015)
COCKATRICE = Enemy(stcustomPath, 290647)
COCKATRICE = Enemy(stcustomPath, 292226)
NEEDLEBIRD = Enemy(stcustomPath, 293805)
NEEDLEBIRD = Enemy(stcustomPath, 295384)
NEEDLEBIRD = Enemy(stcustomPath, 296963)
BIRD = Enemy(stcustomPath, 309595)
BIRD = Enemy(stcustomPath, 311174)
BIRD = Enemy(stcustomPath, 323806)
BIRD = Enemy(stcustomPath, 325385)
LITTLEDEVIL = Enemy(stcustomPath, 326964)
LITTLEDEVIL = Enemy(stcustomPath, 328543)
LITTLEDEVIL = Enemy(stcustomPath, 330122)
LITTLEDEVIL = Enemy(stcustomPath, 331701)
LITTLEDEVIL = Enemy(stcustomPath, 333280)
LITTLEDEVIL = Enemy(stcustomPath, 345912)
LITTLEDEVIL = Enemy(stcustomPath, 347491)
GREMLINS = Enemy(stcustomPath, 349070)
GREMLINS = Enemy(stcustomPath, 350649)
GREMLINS = Enemy(stcustomPath, 352228)
GREMLINS = Enemy(stcustomPath, 353807)
HARPY = Enemy(stcustomPath, 355386)
HARPY = Enemy(stcustomPath, 356965)
HARPY = Enemy(stcustomPath, 358544)
SEIREN = Enemy(stcustomPath, 382229)
ARMORNIGHT = Enemy(stcustomPath, 383808)
ARMORNIGHT = Enemy(stcustomPath, 385387)
ARMORNIGHT = Enemy(stcustomPath, 386966)
ARMORNIGHT = Enemy(stcustomPath, 388545)
ARMORNIGHT = Enemy(stcustomPath, 402756)
SWORDNIGHT = Enemy(stcustomPath, 415388)
SWORDNIGHT = Enemy(stcustomPath, 428020)
SWORDNIGHT = Enemy(stcustomPath, 429599)
DARKLORD = Enemy(stcustomPath, 431178)
DARKLORD = Enemy(stcustomPath, 432757)
NINJA = Enemy(stcustomPath, 434336)
NINJA = Enemy(stcustomPath, 435915)
NINJA = Enemy(stcustomPath, 437494)
NINJA = Enemy(stcustomPath, 439073)
NINJA = Enemy(stcustomPath, 442231)
NINJA = Enemy(stcustomPath, 443810)
NINJAMASTER = Enemy(stcustomPath, 445389)
NINJAMASTER = Enemy(stcustomPath, 446968)
NINJAMASTER = Enemy(stcustomPath, 448547)
NINJAMASTER = Enemy(stcustomPath, 461179)
NINJAMASTER = Enemy(stcustomPath, 462758)
KNIGHTBLADE = Enemy(stcustomPath, 464337)
KNIGHTBLADE = Enemy(stcustomPath, 465916)
EVILSWORD = Enemy(stcustomPath, 467495)
EVILSWORD = Enemy(stcustomPath, 470653)
ELEMENTSWORD = Enemy(stcustomPath, 472232)
ELEMENTSWORD = Enemy(stcustomPath, 473811)
SHAPESHIFTER = Enemy(stcustomPath, 475390)
SHAPESHIFTER = Enemy(stcustomPath, 476969)
SHAPESHIFTER = Enemy(stcustomPath, 478548)
SHADOWZERO = Enemy(stcustomPath, 480127)
SHADOWZERO = Enemy(stcustomPath, 481706)
SPECTRE = Enemy(stcustomPath, 502233)
SPECTRE = Enemy(stcustomPath, 503812)
SPECTRE = Enemy(stcustomPath, 505391)
SPECTRE = Enemy(stcustomPath, 506970)
GHOST = Enemy(stcustomPath, 508549)
GHOST = Enemy(stcustomPath, 510128)
GHOST = Enemy(stcustomPath, 511707)
GHOST = Enemy(stcustomPath, 513286)
DARKPRIEST = Enemy(stcustomPath, 514865)
DARKPRIEST = Enemy(stcustomPath, 516444)
DARKPRIEST = Enemy(stcustomPath, 518023)
DARKPRIEST = Enemy(stcustomPath, 519602)
DARKPRIEST = Enemy(stcustomPath, 521181)
DARKPRIEST = Enemy(stcustomPath, 522760)
DARKPRIEST = Enemy(stcustomPath, 535392)
EVILSHERMAN = Enemy(stcustomPath, 536971)
EVILSHERMAN = Enemy(stcustomPath, 538550)
EVILSHERMAN = Enemy(stcustomPath, 540129)
NECROMANCER = Enemy(stcustomPath, 541708)
NECROMANCER = Enemy(stcustomPath, 543287)
GRELL = Enemy(stcustomPath, 544866)
GRELL = Enemy(stcustomPath, 546445)
GRELL = Enemy(stcustomPath, 548024)
GRELLMAGE = Enemy(stcustomPath, 560656)
PAKKUNOTAMA = Enemy(stcustomPath, 562235)
PAKKUNOTAMA = Enemy(stcustomPath, 563814)
PAKKUNOTAMA = Enemy(stcustomPath, 565393)
PAKKURIOTAMA = Enemy(stcustomPath, 578025)
PAKKUNTOKAGE = Enemy(stcustomPath, 579604)
PAKKUNTOKAGE = Enemy(stcustomPath, 581183)
PAKKUNTOKAGE = Enemy(stcustomPath, 582762)
PAKKUNDRAGON = Enemy(stcustomPath, 595394)
POT = Enemy(stcustomPath, 596973)
POT = Enemy(stcustomPath, 598552)
POT = Enemy(stcustomPath, 600131)
MAMAPOT = Enemy(stcustomPath, 601710)
MAMAPOT = Enemy(stcustomPath, 603289)
MAMAPOT = Enemy(stcustomPath, 615921)
PAPAPOT = Enemy(stcustomPath, 628553)
PAPAPOT = Enemy(stcustomPath, 630132)
PAPAPOT = Enemy(stcustomPath, 631711)
SAHUAGIN = Enemy(stcustomPath, 633290)
SAHUAGIN = Enemy(stcustomPath, 634869)
SAHUAGIN = Enemy(stcustomPath, 647501)
PETITPOSEIDON = Enemy(stcustomPath, 660133)
SEASERPENT = Enemy(stcustomPath, 661712)
SEASERPENT = Enemy(stcustomPath, 663291)
SEADRAGON = Enemy(stcustomPath, 675923)
DUCKSOLDIER = Enemy(stcustomPath, 677502)
DUCKSOLDIER = Enemy(stcustomPath, 679081)
DUCKGENERAL = Enemy(stcustomPath, 691713)
BARETTE = Enemy(stcustomPath, 693292)
GOLDBARETTE = Enemy(stcustomPath, 694871)
GOLDBARETTE = Enemy(stcustomPath, 707503)
FIREDRAKE = Enemy(stcustomPath, 709082)
FIREDRAKE = Enemy(stcustomPath, 721714)
BASILISK = Enemy(stcustomPath, 723293)
BASILISK = Enemy(stcustomPath, 724872)
WEREWOLF = Enemy(stcustomPath, 728030)
WEREWOLF = Enemy(stcustomPath, 729609)
WEREWOLF = Enemy(stcustomPath, 731188)
BLACKFANG = Enemy(stcustomPath, 732767)
BLACKFANG = Enemy(stcustomPath, 734346)
BLACKFANG = Enemy(stcustomPath, 735925)
BLACKFANG = Enemy(stcustomPath, 737504)
SILVERWOLF = Enemy(stcustomPath, 739083)
SILVERWOLF = Enemy(stcustomPath, 751715)
SILVERWOLF = Enemy(stcustomPath, 753294)
BLOODYWOLF = Enemy(stcustomPath, 765926)
BLOODYWOLF = Enemy(stcustomPath, 767505)
BLOODYWOLF = Enemy(stcustomPath, 769084)
WOLFDEVIL = Enemy(stcustomPath, 770663)
WOLFDEVIL = Enemy(stcustomPath, 772242)
WOLFDEVIL = Enemy(stcustomPath, 773821)
MEGACRAWLER = Enemy(stcustomPath, 775400)
MEGACRAWLER = Enemy(stcustomPath, 776979)
GIGACRAWLER = Enemy(stcustomPath, 789611)
GIGACRAWLER = Enemy(stcustomPath, 791190)
PETITDRAGON = Enemy(stcustomPath, 803822)
FROSTDRAGON = Enemy(stcustomPath, 816454)
FROSTDRAGON = Enemy(stcustomPath, 818033)
PETITIAMATT = Enemy(stcustomPath, 819612)
PETITIAMATT = Enemy(stcustomPath, 821191)
PETITIAMATT = Enemy(stcustomPath, 822770)
PETIDRAZOMBIE = Enemy(stcustomPath, 824349)
PETIDRAZOMBIE = Enemy(stcustomPath, 825928)
CARMILLA = Enemy(stcustomPath, 838560)
CARMILLAQUEEN = Enemy(stcustomPath, 840139)
CARMILLAQUEEN = Enemy(stcustomPath, 841718)
CARMILLAQUEEN = Enemy(stcustomPath, 843297)
CARMILLAQUEEN = Enemy(stcustomPath, 844876)
BOULDER = Enemy(stcustomPath, 846455)
POWERBOULDER = Enemy(stcustomPath, 848034)
POWERBOULDER = Enemy(stcustomPath, 849613)
LESSERDAEMON = Enemy(stcustomPath, 851192)
LESSERDAEMON = Enemy(stcustomPath, 852771)
LESSERDAEMON = Enemy(stcustomPath, 854350)
GREATDAEMON = Enemy(stcustomPath, 855929)
GREATDAEMON = Enemy(stcustomPath, 857508)
GREATDAEMON = Enemy(stcustomPath, 859087)
GREATDAEMON = Enemy(stcustomPath, 860666)
GREATDAEMON = Enemy(stcustomPath, 862245)
OGREBOX = Enemy(stcustomPath, 863824)
OGREBOX = Enemy(stcustomPath, 865403)
OGREBOX = Enemy(stcustomPath, 866982)
OGREBOX = Enemy(stcustomPath, 868561)
KAISERMIMIC = Enemy(stcustomPath, 870140)
GREATDAEMON = Enemy(stcustomPath, 871719)
KERBEROS = Enemy(stcustomPath, 873298)
GOLDBARETTE = Enemy(stcustomPath, 874877)
LITTLEDEVIL = Enemy(stcustomPath, 876456)
PETITDRAGON = Enemy(stcustomPath, 878035)
SHAPESHIFTER = Enemy(stcustomPath, 879614)
SHADOWZERO = Enemy(stcustomPath, 881193)
RABI = Enemy(stcustomPath, 882772)
RABIRION = Enemy(stcustomPath, 884351)
KINGRABI = Enemy(stcustomPath, 885930)
GREATRABI = Enemy(stcustomPath, 887509)
KAISERMIMIC = Enemy(stcustomPath, 889088)
HARPY = Enemy(stcustomPath, 890667)
RABI = Enemy(stcustomPath, 892246)
KARL = Enemy(stcustomPath, 893825)
EAGLE = Enemy(stcustomPath, 895404)
Bruiser = Enemy(stcustomPath, 896983)
GOBLIN = Enemy(stcustomPath, 898562)
RABI = Enemy(stcustomPath, 900141)
GUARDIAN = Enemy(stcustomPath, 901720)
GREMLINS = Enemy(stcustomPath, 903299)
KNIGHTBLADE = Enemy(stcustomPath, 904878)
LESSERDAEMON = Enemy(stcustomPath, 906457)
RASTERBUG = Enemy(stcustomPath, 908036)
KERBEROS = Enemy(stcustomPath, 909615)
HIGHWIZARD = Enemy(stcustomPath, 911194)
DEATHMACHINE = Enemy(stcustomPath, 912773)
DARKLORD = Enemy(stcustomPath, 914352)
PETITIAMATT = Enemy(stcustomPath, 915931)
GREATDAEMON = Enemy(stcustomPath, 917510)
RASTERBUG = Enemy(stcustomPath, 919089)
SLIMEPRINCE = Enemy(stcustomPath, 920668)
NIDORION = Enemy(stcustomPath, 922247)
QUEENBEE = Enemy(stcustomPath, 923826)
BASILISK = Enemy(stcustomPath, 925405)
GIGACRAWLER = Enemy(stcustomPath, 926984)
COCKATRICE = Enemy(stcustomPath, 928563)
BIRD = Enemy(stcustomPath, 930142)
WIZARD = Enemy(stcustomPath, 931721)
HIGHWIZARD = Enemy(stcustomPath, 933300)
SWORDNIGHT = Enemy(stcustomPath, 934879)
DARKLORD = Enemy(stcustomPath, 936458)
NINJAMASTER = Enemy(stcustomPath, 938037)
KNIGHTBLADE = Enemy(stcustomPath, 939616)
EVILSHERMAN = Enemy(stcustomPath, 941195)
DUCKGENERAL = Enemy(stcustomPath, 942774)
GOLDBARETTE = Enemy(stcustomPath, 944353)
GREATDAEMON = Enemy(stcustomPath, 945932)
SHAPESHIFTER = Enemy(stcustomPath, 947511)
COCKATRICE = Enemy(stcustomPath, 949090)
BIRD = Enemy(stcustomPath, 950669)
LITTLEDEVIL = Enemy(stcustomPath, 952248)
GREMLINS = Enemy(stcustomPath, 953827)
NINJA = Enemy(stcustomPath, 955406)
NINJAMASTER = Enemy(stcustomPath, 956985)
KNIGHTBLADE = Enemy(stcustomPath, 958564)
EVILSHERMAN = Enemy(stcustomPath, 960143)
DUCKGENERAL = Enemy(stcustomPath, 961722)
GOLDBARETTE = Enemy(stcustomPath, 963301)
GREATDAEMON = Enemy(stcustomPath, 964880)
SHAPESHIFTER = Enemy(stcustomPath, 966459)
ZOMBIE = Enemy(stcustomPath, 968038)
GHOUL = Enemy(stcustomPath, 969617)
GHOST = Enemy(stcustomPath, 971196)
NECROMANCER = Enemy(stcustomPath, 972775)
PETIDRAZOMBIE = Enemy(stcustomPath, 974354)
ZOMBIE = Enemy(stcustomPath, 975933)
GHOUL = Enemy(stcustomPath, 977512)
SLIMEPRINCE = Enemy(stcustomPath, 979091)
GHOST = Enemy(stcustomPath, 980670)
NECROMANCER = Enemy(stcustomPath, 982249)
GRELLMAGE = Enemy(stcustomPath, 983828)
PAKKURIOTAMA = Enemy(stcustomPath, 985407)
PAKKUNDRAGON = Enemy(stcustomPath, 986986)
PETIDRAZOMBIE = Enemy(stcustomPath, 988565)
POWERBOULDER = Enemy(stcustomPath, 990144)
KAISERMIMIC = Enemy(stcustomPath, 991723)
UNICORNHEAD = Enemy(stcustomPath, 993302)
GOLDUNICO = Enemy(stcustomPath, 994881)
HIGHWIZARD = Enemy(stcustomPath, 996460)
GUARDIAN = Enemy(stcustomPath, 998039)
DEATHMACHINE = Enemy(stcustomPath, 999618)
PAPAPOT = Enemy(stcustomPath, 1001197)
PETITPOSEIDON = Enemy(stcustomPath, 1002776)
SAHUAGIN = Enemy(stcustomPath, 1004355)
SEADRAGON = Enemy(stcustomPath, 1005934)
FROSTDRAGON = Enemy(stcustomPath, 1007513)
KAISERMIMIC = Enemy(stcustomPath, 1009092)
UNICORNHEAD = Enemy(stcustomPath, 1010671)
GOLDUNICO = Enemy(stcustomPath, 1012250)
HIGHWIZARD = Enemy(stcustomPath, 1013829)
GUARDIAN = Enemy(stcustomPath, 1015408)
DEATHMACHINE = Enemy(stcustomPath, 1016987)
PAPAPOT = Enemy(stcustomPath, 1018566)
SAHUAGIN = Enemy(stcustomPath, 1020145)
PETITPOSEIDON = Enemy(stcustomPath, 1021724)
SEADRAGON = Enemy(stcustomPath, 1023303)
FROSTDRAGON = Enemy(stcustomPath, 1024882)
SHADOWZERO = Enemy(stcustomPath, 1026461)
DARKBATTOM = Enemy(stcustomPath, 1028040)
BIRD = Enemy(stcustomPath, 1029619)
GREMLINS = Enemy(stcustomPath, 1031198)
SEIREN = Enemy(stcustomPath, 1032777)
ELEMENTSWORD = Enemy(stcustomPath, 1034356)
GIGACRAWLER = Enemy(stcustomPath, 1035935)
CARMILLAQUEEN = Enemy(stcustomPath, 1037514)
POWERBOULDER = Enemy(stcustomPath, 1039093)
LESSERDAEMON = Enemy(stcustomPath, 1040672)
GREATDAEMON = Enemy(stcustomPath, 1042251)
RABI = Enemy(stcustomPath, 1043830)
RABIRION = Enemy(stcustomPath, 1045409)
KINGRABI = Enemy(stcustomPath, 1046988)
GREATRABI = Enemy(stcustomPath, 1048567)
KAISERMIMIC = Enemy(stcustomPath, 1050146)
SAHAGIN = Enemy(stcustomPath, 1051725)


# ****** EnemyStatusStgodstcustom - *****

stgodstcustomPath = r'Game Files\uexp files\Orig\GodEnemyCustomStatusTable.uexp'

DARTHMATANGO_Lv38 = Enemy(stgodstcustomPath, 1690)
DARTHMATANGO_Lv40 = Enemy(stgodstcustomPath, 3269)
DARTHMATANGO_Lv42 = Enemy(stgodstcustomPath, 4848)
DARTHMATANGO_Lv44 = Enemy(stgodstcustomPath, 6427)
DARTHMATANGO_Lv46 = Enemy(stgodstcustomPath, 8006)
DARTHMATANGO_Lv48 = Enemy(stgodstcustomPath, 9585)
DARTHMATANGO_Lv50 = Enemy(stgodstcustomPath, 11164)
BEASTMASTER_Lv38 = Enemy(stgodstcustomPath, 12743)
BEASTMASTER_Lv40 = Enemy(stgodstcustomPath, 14322)
BEASTMASTER_Lv42 = Enemy(stgodstcustomPath, 15901)
BEASTMASTER_Lv44 = Enemy(stgodstcustomPath, 17480)
BEASTMASTER_Lv46 = Enemy(stgodstcustomPath, 19059)
BEASTMASTER_Lv48 = Enemy(stgodstcustomPath, 20638)
BEASTMASTER_Lv50 = Enemy(stgodstcustomPath, 22217)
SUMMON_KERBEROS_Lv38 = Enemy(stgodstcustomPath, 23796)
SUMMON_KERBEROS_Lv40 = Enemy(stgodstcustomPath, 25375)
SUMMON_KERBEROS_Lv42 = Enemy(stgodstcustomPath, 26954)
SUMMON_KERBEROS_Lv44 = Enemy(stgodstcustomPath, 28533)
SUMMON_KERBEROS_Lv46 = Enemy(stgodstcustomPath, 30112)
SUMMON_KERBEROS_Lv48 = Enemy(stgodstcustomPath, 31691)
SUMMON_KERBEROS_Lv50 = Enemy(stgodstcustomPath, 33270)
POROBINLEADER_Lv38 = Enemy(stgodstcustomPath, 34849)
POROBINLEADER_Lv40 = Enemy(stgodstcustomPath, 36428)
POROBINLEADER_Lv42 = Enemy(stgodstcustomPath, 38007)
POROBINLEADER_Lv44 = Enemy(stgodstcustomPath, 39586)
POROBINLEADER_Lv46 = Enemy(stgodstcustomPath, 41165)
POROBINLEADER_Lv48 = Enemy(stgodstcustomPath, 42744)
POROBINLEADER_Lv50 = Enemy(stgodstcustomPath, 44323)
GHOUL_Lv38 = Enemy(stgodstcustomPath, 45902)
GHOUL_Lv40 = Enemy(stgodstcustomPath, 47481)
GHOUL_Lv42 = Enemy(stgodstcustomPath, 49060)
GHOUL_Lv44 = Enemy(stgodstcustomPath, 50639)
GHOUL_Lv46 = Enemy(stgodstcustomPath, 52218)
GHOUL_Lv48 = Enemy(stgodstcustomPath, 53797)
GHOUL_Lv50 = Enemy(stgodstcustomPath, 55376)
SLIMEPRINCE_Lv38 = Enemy(stgodstcustomPath, 56955)
SLIMEPRINCE_Lv40 = Enemy(stgodstcustomPath, 58534)
SLIMEPRINCE_Lv42 = Enemy(stgodstcustomPath, 60113)
SLIMEPRINCE_Lv44 = Enemy(stgodstcustomPath, 61692)
SLIMEPRINCE_Lv46 = Enemy(stgodstcustomPath, 63271)
SLIMEPRINCE_Lv48 = Enemy(stgodstcustomPath, 64850)
SLIMEPRINCE_Lv50 = Enemy(stgodstcustomPath, 66429)
NIDORION_Lv38 = Enemy(stgodstcustomPath, 68008)
NIDORION_Lv40 = Enemy(stgodstcustomPath, 69587)
NIDORION_Lv42 = Enemy(stgodstcustomPath, 71166)
NIDORION_Lv44 = Enemy(stgodstcustomPath, 72745)
NIDORION_Lv46 = Enemy(stgodstcustomPath, 74324)
NIDORION_Lv48 = Enemy(stgodstcustomPath, 75903)
NIDORION_Lv50 = Enemy(stgodstcustomPath, 77482)
QUEENBEE_Lv38 = Enemy(stgodstcustomPath, 79061)
QUEENBEE_Lv40 = Enemy(stgodstcustomPath, 80640)
QUEENBEE_Lv42 = Enemy(stgodstcustomPath, 82219)
QUEENBEE_Lv44 = Enemy(stgodstcustomPath, 83798)
QUEENBEE_Lv46 = Enemy(stgodstcustomPath, 85377)
QUEENBEE_Lv48 = Enemy(stgodstcustomPath, 86956)
QUEENBEE_Lv50 = Enemy(stgodstcustomPath, 88535)
COCKATRICE_Lv38 = Enemy(stgodstcustomPath, 90114)
COCKATRICE_Lv40 = Enemy(stgodstcustomPath, 91693)
COCKATRICE_Lv42 = Enemy(stgodstcustomPath, 93272)
COCKATRICE_Lv44 = Enemy(stgodstcustomPath, 94851)
COCKATRICE_Lv46 = Enemy(stgodstcustomPath, 96430)
COCKATRICE_Lv48 = Enemy(stgodstcustomPath, 98009)
COCKATRICE_Lv50 = Enemy(stgodstcustomPath, 99588)
NEEDLEBIRD_Lv38 = Enemy(stgodstcustomPath, 101167)
NEEDLEBIRD_Lv40 = Enemy(stgodstcustomPath, 102746)
NEEDLEBIRD_Lv42 = Enemy(stgodstcustomPath, 104325)
NEEDLEBIRD_Lv44 = Enemy(stgodstcustomPath, 105904)
NEEDLEBIRD_Lv46 = Enemy(stgodstcustomPath, 107483)
NEEDLEBIRD_Lv48 = Enemy(stgodstcustomPath, 109062)
NEEDLEBIRD_Lv50 = Enemy(stgodstcustomPath, 110641)
COCKATBIRD_Lv38 = Enemy(stgodstcustomPath, 112220)
COCKATBIRD_Lv40 = Enemy(stgodstcustomPath, 113799)
COCKATBIRD_Lv42 = Enemy(stgodstcustomPath, 115378)
COCKATBIRD_Lv44 = Enemy(stgodstcustomPath, 116957)
COCKATBIRD_Lv46 = Enemy(stgodstcustomPath, 118536)
COCKATBIRD_Lv48 = Enemy(stgodstcustomPath, 120115)
COCKATBIRD_Lv50 = Enemy(stgodstcustomPath, 121694)
LITTLEDEVIL_Lv38 = Enemy(stgodstcustomPath, 123273)
LITTLEDEVIL_Lv40 = Enemy(stgodstcustomPath, 124852)
LITTLEDEVIL_Lv42 = Enemy(stgodstcustomPath, 126431)
LITTLEDEVIL_Lv44 = Enemy(stgodstcustomPath, 128010)
LITTLEDEVIL_Lv46 = Enemy(stgodstcustomPath, 129589)
LITTLEDEVIL_Lv48 = Enemy(stgodstcustomPath, 131168)
LITTLEDEVIL_Lv50 = Enemy(stgodstcustomPath, 132747)
UNUSED_HARPY_Lv38 = Enemy(stgodstcustomPath, 134326)
UNUSED_HARPY_Lv40 = Enemy(stgodstcustomPath, 135905)
UNUSED_HARPY_Lv42 = Enemy(stgodstcustomPath, 137484)
UNUSED_HARPY_Lv44 = Enemy(stgodstcustomPath, 139063)
UNUSED_HARPY_Lv46 = Enemy(stgodstcustomPath, 140642)
UNUSED_HARPY_Lv48 = Enemy(stgodstcustomPath, 142221)
UNUSED_HARPY_Lv50 = Enemy(stgodstcustomPath, 143800)
SEIREN_Lv38 = Enemy(stgodstcustomPath, 145379)
SEIREN_Lv40 = Enemy(stgodstcustomPath, 146958)
SEIREN_Lv42 = Enemy(stgodstcustomPath, 148537)
SEIREN_Lv44 = Enemy(stgodstcustomPath, 150116)
SEIREN_Lv46 = Enemy(stgodstcustomPath, 151695)
SEIREN_Lv48 = Enemy(stgodstcustomPath, 153274)
SEIREN_Lv50 = Enemy(stgodstcustomPath, 154853)
UNUSED_ARMORNIGHT_Lv38 = Enemy(stgodstcustomPath, 156432)
UNUSED_ARMORNIGHT_Lv40 = Enemy(stgodstcustomPath, 158011)
UNUSED_ARMORNIGHT_Lv42 = Enemy(stgodstcustomPath, 159590)
UNUSED_ARMORNIGHT_Lv44 = Enemy(stgodstcustomPath, 161169)
UNUSED_ARMORNIGHT_Lv46 = Enemy(stgodstcustomPath, 162748)
UNUSED_ARMORNIGHT_Lv48 = Enemy(stgodstcustomPath, 164327)
UNUSED_ARMORNIGHT_Lv50 = Enemy(stgodstcustomPath, 165906)
SILVERNIGHT_Lv38 = Enemy(stgodstcustomPath, 167485)
SILVERNIGHT_Lv40 = Enemy(stgodstcustomPath, 169064)
SILVERNIGHT_Lv42 = Enemy(stgodstcustomPath, 170643)
SILVERNIGHT_Lv44 = Enemy(stgodstcustomPath, 172222)
SILVERNIGHT_Lv46 = Enemy(stgodstcustomPath, 173801)
SILVERNIGHT_Lv48 = Enemy(stgodstcustomPath, 175380)
SILVERNIGHT_Lv50 = Enemy(stgodstcustomPath, 176959)
SWORDNIGHT_Lv38 = Enemy(stgodstcustomPath, 178538)
SWORDNIGHT_Lv40 = Enemy(stgodstcustomPath, 180117)
SWORDNIGHT_Lv42 = Enemy(stgodstcustomPath, 181696)
SWORDNIGHT_Lv44 = Enemy(stgodstcustomPath, 183275)
SWORDNIGHT_Lv46 = Enemy(stgodstcustomPath, 184854)
SWORDNIGHT_Lv48 = Enemy(stgodstcustomPath, 186433)
SWORDNIGHT_Lv50 = Enemy(stgodstcustomPath, 188012)
NINJAMASTER_Lv38 = Enemy(stgodstcustomPath, 189591)
NINJAMASTER_Lv40 = Enemy(stgodstcustomPath, 191170)
NINJAMASTER_Lv42 = Enemy(stgodstcustomPath, 192749)
NINJAMASTER_Lv44 = Enemy(stgodstcustomPath, 194328)
NINJAMASTER_Lv46 = Enemy(stgodstcustomPath, 195907)
NINJAMASTER_Lv48 = Enemy(stgodstcustomPath, 197486)
NINJAMASTER_Lv50 = Enemy(stgodstcustomPath, 199065)
DARKPRIEST_Lv38 = Enemy(stgodstcustomPath, 200644)
DARKPRIEST_Lv40 = Enemy(stgodstcustomPath, 202223)
DARKPRIEST_Lv42 = Enemy(stgodstcustomPath, 203802)
DARKPRIEST_Lv44 = Enemy(stgodstcustomPath, 205381)
DARKPRIEST_Lv46 = Enemy(stgodstcustomPath, 206960)
DARKPRIEST_Lv48 = Enemy(stgodstcustomPath, 208539)
DARKPRIEST_Lv50 = Enemy(stgodstcustomPath, 210118)
GRELLMAGE_Lv38 = Enemy(stgodstcustomPath, 211697)
GRELLMAGE_Lv40 = Enemy(stgodstcustomPath, 213276)
GRELLMAGE_Lv42 = Enemy(stgodstcustomPath, 214855)
GRELLMAGE_Lv44 = Enemy(stgodstcustomPath, 216434)
GRELLMAGE_Lv46 = Enemy(stgodstcustomPath, 218013)
GRELLMAGE_Lv48 = Enemy(stgodstcustomPath, 219592)
GRELLMAGE_Lv50 = Enemy(stgodstcustomPath, 221171)
PAKKURIOTAMA_Lv38 = Enemy(stgodstcustomPath, 222750)
PAKKURIOTAMA_Lv40 = Enemy(stgodstcustomPath, 224329)
PAKKURIOTAMA_Lv42 = Enemy(stgodstcustomPath, 225908)
PAKKURIOTAMA_Lv44 = Enemy(stgodstcustomPath, 227487)
PAKKURIOTAMA_Lv46 = Enemy(stgodstcustomPath, 229066)
PAKKURIOTAMA_Lv48 = Enemy(stgodstcustomPath, 230645)
PAKKURIOTAMA_Lv50 = Enemy(stgodstcustomPath, 232224)
PAKKUNDRAGON_Lv38 = Enemy(stgodstcustomPath, 233803)
PAKKUNDRAGON_Lv40 = Enemy(stgodstcustomPath, 235382)
PAKKUNDRAGON_Lv42 = Enemy(stgodstcustomPath, 236961)
PAKKUNDRAGON_Lv44 = Enemy(stgodstcustomPath, 238540)
PAKKUNDRAGON_Lv46 = Enemy(stgodstcustomPath, 240119)
PAKKUNDRAGON_Lv48 = Enemy(stgodstcustomPath, 241698)
PAKKUNDRAGON_Lv50 = Enemy(stgodstcustomPath, 243277)
MAMAPOT_Lv38 = Enemy(stgodstcustomPath, 244856)
MAMAPOT_Lv40 = Enemy(stgodstcustomPath, 246435)
MAMAPOT_Lv42 = Enemy(stgodstcustomPath, 248014)
MAMAPOT_Lv44 = Enemy(stgodstcustomPath, 249593)
MAMAPOT_Lv46 = Enemy(stgodstcustomPath, 251172)
MAMAPOT_Lv48 = Enemy(stgodstcustomPath, 252751)
MAMAPOT_Lv50 = Enemy(stgodstcustomPath, 254330)
SUMMON_PAPAPOT_Lv38 = Enemy(stgodstcustomPath, 255909)
SUMMON_PAPAPOT_Lv40 = Enemy(stgodstcustomPath, 257488)
SUMMON_PAPAPOT_Lv42 = Enemy(stgodstcustomPath, 259067)
SUMMON_PAPAPOT_Lv44 = Enemy(stgodstcustomPath, 260646)
SUMMON_PAPAPOT_Lv46 = Enemy(stgodstcustomPath, 262225)
SUMMON_PAPAPOT_Lv48 = Enemy(stgodstcustomPath, 263804)
SUMMON_PAPAPOT_Lv50 = Enemy(stgodstcustomPath, 265383)
SUMMON_SAHUAGIN_Lv38 = Enemy(stgodstcustomPath, 266962)
SUMMON_SAHUAGIN_Lv40 = Enemy(stgodstcustomPath, 268541)
SUMMON_SAHUAGIN_Lv42 = Enemy(stgodstcustomPath, 270120)
SUMMON_SAHUAGIN_Lv44 = Enemy(stgodstcustomPath, 271699)
SUMMON_SAHUAGIN_Lv46 = Enemy(stgodstcustomPath, 273278)
SUMMON_SAHUAGIN_Lv48 = Enemy(stgodstcustomPath, 274857)
SUMMON_SAHUAGIN_Lv50 = Enemy(stgodstcustomPath, 276436)
PETITPOSEIDON_Lv38 = Enemy(stgodstcustomPath, 278015)
PETITPOSEIDON_Lv40 = Enemy(stgodstcustomPath, 279594)
PETITPOSEIDON_Lv42 = Enemy(stgodstcustomPath, 281173)
PETITPOSEIDON_Lv44 = Enemy(stgodstcustomPath, 282752)
PETITPOSEIDON_Lv46 = Enemy(stgodstcustomPath, 284331)
PETITPOSEIDON_Lv48 = Enemy(stgodstcustomPath, 285910)
PETITPOSEIDON_Lv50 = Enemy(stgodstcustomPath, 287489)
SEADRAGON_Lv38 = Enemy(stgodstcustomPath, 289068)
SEADRAGON_Lv40 = Enemy(stgodstcustomPath, 290647)
SEADRAGON_Lv42 = Enemy(stgodstcustomPath, 292226)
SEADRAGON_Lv44 = Enemy(stgodstcustomPath, 293805)
SEADRAGON_Lv46 = Enemy(stgodstcustomPath, 295384)
SEADRAGON_Lv48 = Enemy(stgodstcustomPath, 296963)
SEADRAGON_Lv50 = Enemy(stgodstcustomPath, 298542)
DUCKGENERAL_Lv38 = Enemy(stgodstcustomPath, 300121)
DUCKGENERAL_Lv40 = Enemy(stgodstcustomPath, 301700)
DUCKGENERAL_Lv42 = Enemy(stgodstcustomPath, 303279)
DUCKGENERAL_Lv44 = Enemy(stgodstcustomPath, 304858)
DUCKGENERAL_Lv46 = Enemy(stgodstcustomPath, 306437)
DUCKGENERAL_Lv48 = Enemy(stgodstcustomPath, 308016)
DUCKGENERAL_Lv50 = Enemy(stgodstcustomPath, 309595)
SUMMON_GOLDBARETTE_Lv38 = Enemy(stgodstcustomPath, 311174)
SUMMON_GOLDBARETTE_Lv40 = Enemy(stgodstcustomPath, 312753)
SUMMON_GOLDBARETTE_Lv42 = Enemy(stgodstcustomPath, 314332)
SUMMON_GOLDBARETTE_Lv44 = Enemy(stgodstcustomPath, 315911)
SUMMON_GOLDBARETTE_Lv46 = Enemy(stgodstcustomPath, 317490)
SUMMON_GOLDBARETTE_Lv48 = Enemy(stgodstcustomPath, 319069)
SUMMON_GOLDBARETTE_Lv50 = Enemy(stgodstcustomPath, 320648)
FIREDRAKE_Lv38 = Enemy(stgodstcustomPath, 322227)
FIREDRAKE_Lv40 = Enemy(stgodstcustomPath, 323806)
FIREDRAKE_Lv42 = Enemy(stgodstcustomPath, 325385)
FIREDRAKE_Lv44 = Enemy(stgodstcustomPath, 326964)
FIREDRAKE_Lv46 = Enemy(stgodstcustomPath, 328543)
FIREDRAKE_Lv48 = Enemy(stgodstcustomPath, 330122)
FIREDRAKE_Lv50 = Enemy(stgodstcustomPath, 331701)
SILVERWOLF_Lv38 = Enemy(stgodstcustomPath, 333280)
SILVERWOLF_Lv40 = Enemy(stgodstcustomPath, 334859)
SILVERWOLF_Lv42 = Enemy(stgodstcustomPath, 336438)
SILVERWOLF_Lv44 = Enemy(stgodstcustomPath, 338017)
SILVERWOLF_Lv46 = Enemy(stgodstcustomPath, 339596)
SILVERWOLF_Lv48 = Enemy(stgodstcustomPath, 341175)
SILVERWOLF_Lv50 = Enemy(stgodstcustomPath, 342754)
BLOODYWOLF_Lv38 = Enemy(stgodstcustomPath, 344333)
BLOODYWOLF_Lv40 = Enemy(stgodstcustomPath, 345912)
BLOODYWOLF_Lv42 = Enemy(stgodstcustomPath, 347491)
BLOODYWOLF_Lv44 = Enemy(stgodstcustomPath, 349070)
BLOODYWOLF_Lv46 = Enemy(stgodstcustomPath, 350649)
BLOODYWOLF_Lv48 = Enemy(stgodstcustomPath, 352228)
BLOODYWOLF_Lv50 = Enemy(stgodstcustomPath, 353807)
GIGACRAWLER_Lv38 = Enemy(stgodstcustomPath, 355386)
GIGACRAWLER_Lv40 = Enemy(stgodstcustomPath, 356965)
GIGACRAWLER_Lv42 = Enemy(stgodstcustomPath, 358544)
GIGACRAWLER_Lv44 = Enemy(stgodstcustomPath, 360123)
GIGACRAWLER_Lv46 = Enemy(stgodstcustomPath, 361702)
GIGACRAWLER_Lv48 = Enemy(stgodstcustomPath, 363281)
GIGACRAWLER_Lv50 = Enemy(stgodstcustomPath, 364860)
PETITDRAGON_Lv38 = Enemy(stgodstcustomPath, 366439)
PETITDRAGON_Lv40 = Enemy(stgodstcustomPath, 368018)
PETITDRAGON_Lv42 = Enemy(stgodstcustomPath, 369597)
PETITDRAGON_Lv44 = Enemy(stgodstcustomPath, 371176)
PETITDRAGON_Lv46 = Enemy(stgodstcustomPath, 372755)
PETITDRAGON_Lv48 = Enemy(stgodstcustomPath, 374334)
PETITDRAGON_Lv50 = Enemy(stgodstcustomPath, 375913)
FROSTDRAGON_Lv38 = Enemy(stgodstcustomPath, 377492)
FROSTDRAGON_Lv40 = Enemy(stgodstcustomPath, 379071)
FROSTDRAGON_Lv42 = Enemy(stgodstcustomPath, 380650)
FROSTDRAGON_Lv44 = Enemy(stgodstcustomPath, 382229)
FROSTDRAGON_Lv46 = Enemy(stgodstcustomPath, 383808)
FROSTDRAGON_Lv48 = Enemy(stgodstcustomPath, 385387)
FROSTDRAGON_Lv50 = Enemy(stgodstcustomPath, 386966)
CARMILLA_Lv38 = Enemy(stgodstcustomPath, 388545)
CARMILLA_Lv40 = Enemy(stgodstcustomPath, 390124)
CARMILLA_Lv42 = Enemy(stgodstcustomPath, 391703)
CARMILLA_Lv44 = Enemy(stgodstcustomPath, 393282)
CARMILLA_Lv46 = Enemy(stgodstcustomPath, 394861)
CARMILLA_Lv48 = Enemy(stgodstcustomPath, 396440)
CARMILLA_Lv50 = Enemy(stgodstcustomPath, 398019)
OGREBOX_Lv38 = Enemy(stgodstcustomPath, 399598)
OGREBOX_Lv40 = Enemy(stgodstcustomPath, 401177)
OGREBOX_Lv42 = Enemy(stgodstcustomPath, 402756)
OGREBOX_Lv44 = Enemy(stgodstcustomPath, 404335)
OGREBOX_Lv46 = Enemy(stgodstcustomPath, 405914)
OGREBOX_Lv48 = Enemy(stgodstcustomPath, 407493)
OGREBOX_Lv50 = Enemy(stgodstcustomPath, 409072)


# ********** Files in ...\Data\Csv\CharaData **********

# ****** EnemyStatusStEnStat - *****

stEnStatPath = r'Game Files\uexp files\Orig\EnemyStatusTable.uexp'

RABI = Enemy(stEnStatPath, 111)
RABIRION = Enemy(stEnStatPath, 1690)
KINGRABI = Enemy(stEnStatPath, 3269)
GREATRABI = Enemy(stEnStatPath, 4848)
MAIKONIDO = Enemy(stEnStatPath, 6427)
DARTHMATANGO = Enemy(stEnStatPath, 8006)
BATTOM = Enemy(stEnStatPath, 9585)
DARKBATTOM = Enemy(stEnStatPath, 11164)
GOBLIN = Enemy(stEnStatPath, 12743)
GOBLINLORD = Enemy(stEnStatPath, 14322)
BEASTMASTER = Enemy(stEnStatPath, 15901)
BOUNDWOLF = Enemy(stEnStatPath, 17480)
KERBEROS = Enemy(stEnStatPath, 19059)
ASSASSINBUG = Enemy(stEnStatPath, 20638)
RASTERBUG = Enemy(stEnStatPath, 22217)
PORON = Enemy(stEnStatPath, 23796)
POROBINHOOD = Enemy(stEnStatPath, 25375)
POROBINLEADER = Enemy(stEnStatPath, 26954)
ZOMBIE = Enemy(stEnStatPath, 28533)
GHOUL = Enemy(stEnStatPath, 30112)
SLIME = Enemy(stEnStatPath, 31691)
SLIMEPRINCE = Enemy(stEnStatPath, 33270)
MALLBEAR = Enemy(stEnStatPath, 34849)
NIDORION = Enemy(stEnStatPath, 36428)
GALBEE = Enemy(stEnStatPath, 38007)
LADYBEE = Enemy(stEnStatPath, 39586)
QUEENBEE = Enemy(stEnStatPath, 41165)
UNICORNHEAD = Enemy(stEnStatPath, 42744)
GOLDUNICO = Enemy(stEnStatPath, 44323)
MAGICIAN = Enemy(stEnStatPath, 45902)
WIZARD = Enemy(stEnStatPath, 47481)
HIGHWIZARD = Enemy(stEnStatPath, 49060)
MACHINEGOLEM = Enemy(stEnStatPath, 50639)
GUARDIAN = Enemy(stEnStatPath, 52218)
DEATHMACHINE = Enemy(stEnStatPath, 53797)
COCKATRICE = Enemy(stEnStatPath, 55376)
NEEDLEBIRD = Enemy(stEnStatPath, 56955)
BIRD = Enemy(stEnStatPath, 58534)
LITTLEDEVIL = Enemy(stEnStatPath, 60113)
GREMLINS = Enemy(stEnStatPath, 61692)
HARPY = Enemy(stEnStatPath, 63271)
SEIREN = Enemy(stEnStatPath, 64850)
ARMORNIGHT = Enemy(stEnStatPath, 66429)
SILVERNIGHT = Enemy(stEnStatPath, 68008)
SWORDNIGHT = Enemy(stEnStatPath, 69587)
DARKLORD = Enemy(stEnStatPath, 71166)
NINJA = Enemy(stEnStatPath, 72745)
NINJAMASTER = Enemy(stEnStatPath, 74324)
KNIGHTBLADE = Enemy(stEnStatPath, 75903)
EVILSWORD = Enemy(stEnStatPath, 77482)
ELEMENTSWORD = Enemy(stEnStatPath, 79061)
SHAPESHIFTER = Enemy(stEnStatPath, 80640)
SHADOWZERO = Enemy(stEnStatPath, 82219)
SPECTRE = Enemy(stEnStatPath, 93272)
GHOST = Enemy(stEnStatPath, 94851)
DARKPRIEST = Enemy(stEnStatPath, 96430)
EVILSHERMAN = Enemy(stEnStatPath, 98009)
NECROMANCER = Enemy(stEnStatPath, 99588)
GRELL = Enemy(stEnStatPath, 101167)
GRELLMAGE = Enemy(stEnStatPath, 102746)
PAKKUNOTAMA = Enemy(stEnStatPath, 104325)
PAKKURIOTAMA = Enemy(stEnStatPath, 105904)
PAKKUNTOKAGE = Enemy(stEnStatPath, 107483)
PAKKUNDRAGON = Enemy(stEnStatPath, 109062)
POT = Enemy(stEnStatPath, 110641)
MAMAPOT = Enemy(stEnStatPath, 112220)
PAPAPOT = Enemy(stEnStatPath, 113799)
SAHUAGIN = Enemy(stEnStatPath, 115378)
PETITPOSEIDON = Enemy(stEnStatPath, 116957)
SEASERPENT = Enemy(stEnStatPath, 118536)
SEADRAGON = Enemy(stEnStatPath, 120115)
DUCKSOLDIER = Enemy(stEnStatPath, 121694)
DUCKGENERAL = Enemy(stEnStatPath, 123273)
BARETTE = Enemy(stEnStatPath, 124852)
GOLDBARETTE = Enemy(stEnStatPath, 126431)
FIREDRAKE = Enemy(stEnStatPath, 128010)
BASILISK = Enemy(stEnStatPath, 129589)
WEREWOLF = Enemy(stEnStatPath, 131168)
BLACKFANG = Enemy(stEnStatPath, 132747)
SILVERWOLF = Enemy(stEnStatPath, 134326)
BLOODYWOLF = Enemy(stEnStatPath, 135905)
WOLFDEVIL = Enemy(stEnStatPath, 137484)
MEGACRAWLER = Enemy(stEnStatPath, 139063)
GIGACRAWLER = Enemy(stEnStatPath, 140642)
PETITDRAGON = Enemy(stEnStatPath, 142221)
FROSTDRAGON = Enemy(stEnStatPath, 143800)
PETITIAMATT = Enemy(stEnStatPath, 145379)
PETIDRAZOMBIE = Enemy(stEnStatPath, 146958)
CARMILLA = Enemy(stEnStatPath, 148537)
CARMILLAQUEEN = Enemy(stEnStatPath, 150116)
BOULDER = Enemy(stEnStatPath, 151695)
POWERBOULDER = Enemy(stEnStatPath, 153274)
LESSERDAEMON = Enemy(stEnStatPath, 154853)
GREATDAEMON = Enemy(stEnStatPath, 156432)
OGREBOX = Enemy(stEnStatPath, 158011)
KAISERMIMIC = Enemy(stEnStatPath, 159590)
Karl = Enemy(stEnStatPath, 162748)
Eagle = Enemy(stEnStatPath, 164327)
Bruiser = Enemy(stEnStatPath, 165906)
Bruiser2 = Enemy(stEnStatPath, 167485)


# ****** EnemyStatusStMaxStat - *****

stMaxStatPath = r'Game Files\uexp files\Orig\EnemyStatusMaxTable.uexp'

RABI = Enemy(stMaxStatPath, 111)
RABIRION = Enemy(stMaxStatPath, 1690)
KINGRABI = Enemy(stMaxStatPath, 3269)
GREATRABI = Enemy(stMaxStatPath, 4848)
MAIKONIDO = Enemy(stMaxStatPath, 6427)
DARTHMATANGO = Enemy(stMaxStatPath, 8006)
BATTOM = Enemy(stMaxStatPath, 9585)
DARKBATTOM = Enemy(stMaxStatPath, 11164)
GOBLIN = Enemy(stMaxStatPath, 12743)
GOBLINLORD = Enemy(stMaxStatPath, 14322)
BEASTMASTER = Enemy(stMaxStatPath, 15901)
BOUNDWOLF = Enemy(stMaxStatPath, 17480)
KERBEROS = Enemy(stMaxStatPath, 19059)
ASSASSINBUG = Enemy(stMaxStatPath, 20638)
RASTERBUG = Enemy(stMaxStatPath, 22217)
PORON = Enemy(stMaxStatPath, 23796)
POROBINHOOD = Enemy(stMaxStatPath, 25375)
POROBINLEADER = Enemy(stMaxStatPath, 26954)
ZOMBIE = Enemy(stMaxStatPath, 28533)
GHOUL = Enemy(stMaxStatPath, 30112)
SLIME = Enemy(stMaxStatPath, 31691)
SLIMEPRINCE = Enemy(stMaxStatPath, 33270)
MALLBEAR = Enemy(stMaxStatPath, 34849)
NIDORION = Enemy(stMaxStatPath, 36428)
GALBEE = Enemy(stMaxStatPath, 38007)
LADYBEE = Enemy(stMaxStatPath, 39586)
QUEENBEE = Enemy(stMaxStatPath, 41165)
UNICORNHEAD = Enemy(stMaxStatPath, 42744)
GOLDUNICO = Enemy(stMaxStatPath, 44323)
MAGICIAN = Enemy(stMaxStatPath, 45902)
WIZARD = Enemy(stMaxStatPath, 47481)
HIGHWIZARD = Enemy(stMaxStatPath, 49060)
MACHINEGOLEM = Enemy(stMaxStatPath, 50639)
GUARDIAN = Enemy(stMaxStatPath, 52218)
DEATHMACHINE = Enemy(stMaxStatPath, 53797)
COCKATRICE = Enemy(stMaxStatPath, 55376)
NEEDLEBIRD = Enemy(stMaxStatPath, 56955)
BIRD = Enemy(stMaxStatPath, 58534)
LITTLEDEVIL = Enemy(stMaxStatPath, 60113)
GREMLINS = Enemy(stMaxStatPath, 61692)
HARPY = Enemy(stMaxStatPath, 63271)
SEIREN = Enemy(stMaxStatPath, 64850)
ARMORNIGHT = Enemy(stMaxStatPath, 66429)
SILVERNIGHT = Enemy(stMaxStatPath, 68008)
SWORDNIGHT = Enemy(stMaxStatPath, 69587)
DARKLORD = Enemy(stMaxStatPath, 71166)
NINJA = Enemy(stMaxStatPath, 72745)
NINJAMASTER = Enemy(stMaxStatPath, 74324)
KNIGHTBLADE = Enemy(stMaxStatPath, 75903)
EVILSWORD = Enemy(stMaxStatPath, 77482)
ELEMENTSWORD = Enemy(stMaxStatPath, 79061)
SHAPESHIFTER = Enemy(stMaxStatPath, 80640)
SHADOWZERO = Enemy(stMaxStatPath, 82219)
SPECTRE = Enemy(stMaxStatPath, 93272)
GHOST = Enemy(stMaxStatPath, 94851)
DARKPRIEST = Enemy(stMaxStatPath, 96430)
EVILSHERMAN = Enemy(stMaxStatPath, 98009)
NECROMANCER = Enemy(stMaxStatPath, 99588)
GRELL = Enemy(stMaxStatPath, 101167)
GRELLMAGE = Enemy(stMaxStatPath, 102746)
PAKKUNOTAMA = Enemy(stMaxStatPath, 104325)
PAKKURIOTAMA = Enemy(stMaxStatPath, 105904)
PAKKUNTOKAGE = Enemy(stMaxStatPath, 107483)
PAKKUNDRAGON = Enemy(stMaxStatPath, 109062)
POT = Enemy(stMaxStatPath, 110641)
MAMAPOT = Enemy(stMaxStatPath, 112220)
PAPAPOT = Enemy(stMaxStatPath, 113799)
SAHUAGIN = Enemy(stMaxStatPath, 115378)
PETITPOSEIDON = Enemy(stMaxStatPath, 116957)
SEASERPENT = Enemy(stMaxStatPath, 118536)
SEADRAGON = Enemy(stMaxStatPath, 120115)
DUCKSOLDIER = Enemy(stMaxStatPath, 121694)
DUCKGENERAL = Enemy(stMaxStatPath, 123273)
BARETTE = Enemy(stMaxStatPath, 124852)
GOLDBARETTE = Enemy(stMaxStatPath, 126431)
FIREDRAKE = Enemy(stMaxStatPath, 128010)
BASILISK = Enemy(stMaxStatPath, 129589)
WEREWOLF = Enemy(stMaxStatPath, 131168)
BLACKFANG = Enemy(stMaxStatPath, 132747)
SILVERWOLF = Enemy(stMaxStatPath, 134326)
BLOODYWOLF = Enemy(stMaxStatPath, 135905)
WOLFDEVIL = Enemy(stMaxStatPath, 137484)
MEGACRAWLER = Enemy(stMaxStatPath, 139063)
GIGACRAWLER = Enemy(stMaxStatPath, 140642)
PETITDRAGON = Enemy(stMaxStatPath, 142221)
FROSTDRAGON = Enemy(stMaxStatPath, 143800)
PETITIAMATT = Enemy(stMaxStatPath, 145379)
PETIDRAZOMBIE = Enemy(stMaxStatPath, 146958)
CARMILLA = Enemy(stMaxStatPath, 148537)
CARMILLAQUEEN = Enemy(stMaxStatPath, 150116)
BOULDER = Enemy(stMaxStatPath, 151695)
POWERBOULDER = Enemy(stMaxStatPath, 153274)
LESSERDAEMON = Enemy(stMaxStatPath, 154853)
GREATDAEMON = Enemy(stMaxStatPath, 156432)
OGREBOX = Enemy(stMaxStatPath, 158011)
KAISERMIMIC = Enemy(stMaxStatPath, 159590)
Karl = Enemy(stMaxStatPath, 162748)
Eagle = Enemy(stMaxStatPath, 164327)
Bruiser = Enemy(stMaxStatPath, 165906)
Bruiser2 = Enemy(stMaxStatPath, 167485)
#endregion


#region Boss Instance Creation Start

# Charadata
# ****** BossStatusStbossSt - *****

stbossStPath = r'Game Files\Boss\Orig\uexp files\Charadata\BossStatusTable.uexp'

FullmetalHugger = Boss(stbossStPath, 140)
MachineGolemR = Boss(stbossStPath, 1764)
Jewel_EaterR = Boss(stbossStPath, 3388)
Zhenker = Boss(stbossStPath, 5012)
Genoa = Boss(stbossStPath, 6636)
Bill = Boss(stbossStPath, 8260)
Ben = Boss(stbossStPath, 9884)
Bill_and_Ben = Boss(stbossStPath, 11508)
Gorva = Boss(stbossStPath, 13132)
MachineGolemS = Boss(stbossStPath, 14756)
Beast_Ruger = Boss(stbossStPath, 16380)
Guilder_Vine = Boss(stbossStPath, 18004)
Land_amber = Boss(stbossStPath, 19628)
Feegu_Mund = Boss(stbossStPath, 21252)
Zan_Bie = Boss(stbossStPath, 22876)
Dangard = Boss(stbossStPath, 24500)
Mispolm = Boss(stbossStPath, 26124)
Doran = Boss(stbossStPath, 27748)
Light_Geizer = Boss(stbossStPath, 29372)
Sablehor = Boss(stbossStPath, 30996)
BlackKnight = Boss(stbossStPath, 32620)
CrimsonWizard = Boss(stbossStPath, 34244)
CrimsonWizardEvent = Boss(stbossStPath, 35868)
Man_eating_death = Boss(stbossStPath, 37492)
Fallen_saint = Boss(stbossStPath, 39116)
Earl_of_evil_eye = Boss(stbossStPath, 40740)
JewelryBeast = Boss(stbossStPath, 42364)
HugeDragon = Boss(stbossStPath, 43988)
DarkRich = Boss(stbossStPath, 45612)
ArchDemon = Boss(stbossStPath, 47236)
BlackRabi = Boss(stbossStPath, 48860)
MiniBlackRabi = Boss(stbossStPath, 50484)
Bruiser = Boss(stbossStPath, 52108)
Karl = Boss(stbossStPath, 53732)
Bill = Boss(stbossStPath, 55356)
Ben = Boss(stbossStPath, 56980)
Bill_and_Ben = Boss(stbossStPath, 58604)
Gorva = Boss(stbossStPath, 60228)
FullmetalHugger = Boss(stbossStPath, 61852)
Man_eating_death_Avatar = Boss(stbossStPath, 63476)
Jewel_Eater = Boss(stbossStPath, 65100)
Zhenker = Boss(stbossStPath, 66724)
Genoa = Boss(stbossStPath, 68348)
Guilder_Vine = Boss(stbossStPath, 69972)
Anise = Boss(stbossStPath, 71596)
AniseDragon = Boss(stbossStPath, 73220)
Sablehor_BlueMan = Boss(stbossStPath, 74844)
Sablehor_PurpleMan = Boss(stbossStPath, 76468)
ManaStone_Earth = Boss(stbossStPath, 78092)
ManaStone_Water = Boss(stbossStPath, 79716)
ManaStone_Fire = Boss(stbossStPath, 81340)
ManaStone_Wind = Boss(stbossStPath, 82964)
Anise_Avatar = Boss(stbossStPath, 84588)
ManaStone_Black = Boss(stbossStPath, 86212)
Mispolm_Ivy = Boss(stbossStPath, 87836)
Roki = Boss(stbossStPath, 89460)
BeastKing = Boss(stbossStPath, 91084)
Crystal = Boss(stbossStPath, 92708)
ArchDemon_ArmL = Boss(stbossStPath, 94332)
ArchDemon_ArmR = Boss(stbossStPath, 95956)
FullmetalHugger = Boss(stbossStPath, 97580)
Zhenker = Boss(stbossStPath, 99204)
Genoa = Boss(stbossStPath, 100828)
#endregion


#region Shinju Instance Creation Start

# ShinjuStatusTableList

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb11_CustomStatusTable.uexp'
Land_amber = Shinju(stshinjuCustomPath, 140)
Land_amber = Shinju(stshinjuCustomPath, 1764)
Land_amber = Shinju(stshinjuCustomPath, 3388)
Land_amber = Shinju(stshinjuCustomPath, 5012)
Land_amber = Shinju(stshinjuCustomPath, 6636)
Land_amber = Shinju(stshinjuCustomPath, 8260)
Land_amber = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb12_CustomStatusTable.uexp'
Feegu_Mund = Shinju(stshinjuCustomPath, 140)
Feegu_Mund = Shinju(stshinjuCustomPath, 1764)
Feegu_Mund = Shinju(stshinjuCustomPath, 3388)
Feegu_Mund = Shinju(stshinjuCustomPath, 5012)
Feegu_Mund = Shinju(stshinjuCustomPath, 6636)
Feegu_Mund = Shinju(stshinjuCustomPath, 8260)
Feegu_Mund = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb13_CustomStatusTable.uexp'
Zan_Bie = Shinju(stshinjuCustomPath, 140)
Zan_Bie = Shinju(stshinjuCustomPath, 1764)
Zan_Bie = Shinju(stshinjuCustomPath, 3388)
Zan_Bie = Shinju(stshinjuCustomPath, 5012)
Zan_Bie = Shinju(stshinjuCustomPath, 6636)
Zan_Bie = Shinju(stshinjuCustomPath, 8260)
Zan_Bie = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb14_CustomStatusTable.uexp'
Dangard = Shinju(stshinjuCustomPath, 140)
Dangard = Shinju(stshinjuCustomPath, 1764)
Dangard = Shinju(stshinjuCustomPath, 3388)
Dangard = Shinju(stshinjuCustomPath, 5012)
Dangard = Shinju(stshinjuCustomPath, 6636)
Dangard = Shinju(stshinjuCustomPath, 8260)
Dangard = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb15_02_CustomStatusTable.uexp'
Mispolm = Shinju(stshinjuCustomPath, 140)
Mispolm = Shinju(stshinjuCustomPath, 1764)
Mispolm = Shinju(stshinjuCustomPath, 3388)
Mispolm = Shinju(stshinjuCustomPath, 5012)
Mispolm = Shinju(stshinjuCustomPath, 6636)
Mispolm = Shinju(stshinjuCustomPath, 8260)
Mispolm = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb15_CustomStatusTable.uexp'
Mispolm = Shinju(stshinjuCustomPath, 140)
Mispolm = Shinju(stshinjuCustomPath, 1764)
Mispolm = Shinju(stshinjuCustomPath, 3388)
Mispolm = Shinju(stshinjuCustomPath, 5012)
Mispolm = Shinju(stshinjuCustomPath, 6636)
Mispolm = Shinju(stshinjuCustomPath, 8260)
Mispolm = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb16_CustomStatusTable.uexp'
Doran = Shinju(stshinjuCustomPath, 140)
Doran = Shinju(stshinjuCustomPath, 1764)
Doran = Shinju(stshinjuCustomPath, 3388)
Doran = Shinju(stshinjuCustomPath, 5012)
Doran = Shinju(stshinjuCustomPath, 6636)
Doran = Shinju(stshinjuCustomPath, 8260)
Doran = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb17_CustomStatusTable.uexp'
Light_Geizer = Shinju(stshinjuCustomPath, 140)
Light_Geizer = Shinju(stshinjuCustomPath, 1764)
Light_Geizer = Shinju(stshinjuCustomPath, 3388)
Light_Geizer = Shinju(stshinjuCustomPath, 5012)
Light_Geizer = Shinju(stshinjuCustomPath, 6636)
Light_Geizer = Shinju(stshinjuCustomPath, 8260)
Light_Geizer = Shinju(stshinjuCustomPath, 9884)

# ****** ShinjuStatusSteb_11Parts0 - *****
steb_11Parts0Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\01_eb11_01_PartsStatusTable.uexp'
Body = Shinju(steb_11Parts0Path, 111)
ArmL = Shinju(steb_11Parts0Path, 1690)
ArmR = Shinju(steb_11Parts0Path, 3269)
ArmL_Core01 = Shinju(steb_11Parts0Path, 4848)
ArmL_Core02 = Shinju(steb_11Parts0Path, 6427)
ArmR_Core01 = Shinju(steb_11Parts0Path, 8006)
ArmR_Core02 = Shinju(steb_11Parts0Path, 9585)

# ****** ShinjuStatusSteb_11Parts1 - *****
steb_11Parts1Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\02_eb11_01_PartsStatusTable.uexp'
Body = Shinju(steb_11Parts1Path, 111)
ArmL = Shinju(steb_11Parts1Path, 1690)
ArmR = Shinju(steb_11Parts1Path, 3269)
ArmL_Core01 = Shinju(steb_11Parts1Path, 4848)
ArmL_Core02 = Shinju(steb_11Parts1Path, 6427)
ArmR_Core01 = Shinju(steb_11Parts1Path, 8006)
ArmR_Core02 = Shinju(steb_11Parts1Path, 9585)

# ****** ShinjuStatusSteb_11Parts2 - *****
steb_11Parts2Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\03_eb11_01_PartsStatusTable.uexp'
Body = Shinju(steb_11Parts2Path, 111)
ArmL = Shinju(steb_11Parts2Path, 1690)
ArmR = Shinju(steb_11Parts2Path, 3269)
ArmL_Core01 = Shinju(steb_11Parts2Path, 4848)
ArmL_Core02 = Shinju(steb_11Parts2Path, 6427)
ArmR_Core01 = Shinju(steb_11Parts2Path, 8006)
ArmR_Core02 = Shinju(steb_11Parts2Path, 9585)

# ****** ShinjuStatusSteb_11Parts3 - *****
steb_11Parts3Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\04_eb11_01_PartsStatusTable.uexp'
Body = Shinju(steb_11Parts3Path, 111)
ArmL = Shinju(steb_11Parts3Path, 1690)
ArmR = Shinju(steb_11Parts3Path, 3269)
ArmL_Core01 = Shinju(steb_11Parts3Path, 4848)
ArmL_Core02 = Shinju(steb_11Parts3Path, 6427)
ArmR_Core01 = Shinju(steb_11Parts3Path, 8006)
ArmR_Core02 = Shinju(steb_11Parts3Path, 9585)

# ****** ShinjuStatusSteb_11Parts4 - *****
steb_11Parts4Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\05_eb11_01_PartsStatusTable.uexp'
Body = Shinju(steb_11Parts4Path, 111)
ArmL = Shinju(steb_11Parts4Path, 1690)
ArmR = Shinju(steb_11Parts4Path, 3269)
ArmL_Core01 = Shinju(steb_11Parts4Path, 4848)
ArmL_Core02 = Shinju(steb_11Parts4Path, 6427)
ArmR_Core01 = Shinju(steb_11Parts4Path, 8006)
ArmR_Core02 = Shinju(steb_11Parts4Path, 9585)

# ****** ShinjuStatusSteb_11Parts5 - *****
steb_11Parts5Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\06_eb11_01_PartsStatusTable.uexp'
Body = Shinju(steb_11Parts5Path, 111)
ArmL = Shinju(steb_11Parts5Path, 1690)
ArmR = Shinju(steb_11Parts5Path, 3269)
ArmL_Core01 = Shinju(steb_11Parts5Path, 4848)
ArmL_Core02 = Shinju(steb_11Parts5Path, 6427)
ArmR_Core01 = Shinju(steb_11Parts5Path, 8006)
ArmR_Core02 = Shinju(steb_11Parts5Path, 9585)

# ****** ShinjuStatusSteb_11Parts6 - *****
steb_11Parts6Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\07_eb11_01_PartsStatusTable.uexp'
Body = Shinju(steb_11Parts6Path, 111)
ArmL = Shinju(steb_11Parts6Path, 1690)
ArmR = Shinju(steb_11Parts6Path, 3269)
ArmL_Core01 = Shinju(steb_11Parts6Path, 4848)
ArmL_Core02 = Shinju(steb_11Parts6Path, 6427)
ArmR_Core01 = Shinju(steb_11Parts6Path, 8006)
ArmR_Core02 = Shinju(steb_11Parts6Path, 9585)

# ****** ShinjuStatusSteb_12Parts7 - *****
steb_12Parts7Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\01_eb12_01_PartsStatusTable.uexp'
Head = Shinju(steb_12Parts7Path, 111)
Body = Shinju(steb_12Parts7Path, 1690)
ArmL = Shinju(steb_12Parts7Path, 3269)
ArmR = Shinju(steb_12Parts7Path, 4848)
Tail = Shinju(steb_12Parts7Path, 6427)

# ****** ShinjuStatusSteb_12Parts8 - *****
steb_12Parts8Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\02_eb12_01_PartsStatusTable.uexp'
Head = Shinju(steb_12Parts8Path, 111)
Body = Shinju(steb_12Parts8Path, 1690)
ArmL = Shinju(steb_12Parts8Path, 3269)
ArmR = Shinju(steb_12Parts8Path, 4848)
Tail = Shinju(steb_12Parts8Path, 6427)

# ****** ShinjuStatusSteb_12Parts9 - *****
steb_12Parts9Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\03_eb12_01_PartsStatusTable.uexp'
Head = Shinju(steb_12Parts9Path, 111)
Body = Shinju(steb_12Parts9Path, 1690)
ArmL = Shinju(steb_12Parts9Path, 3269)
ArmR = Shinju(steb_12Parts9Path, 4848)
Tail = Shinju(steb_12Parts9Path, 6427)

# ****** ShinjuStatusSteb_12Parts10 - *****
steb_12Parts10Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\04_eb12_01_PartsStatusTable.uexp'
Head = Shinju(steb_12Parts10Path, 111)
Body = Shinju(steb_12Parts10Path, 1690)
ArmL = Shinju(steb_12Parts10Path, 3269)
ArmR = Shinju(steb_12Parts10Path, 4848)
Tail = Shinju(steb_12Parts10Path, 6427)

# ****** ShinjuStatusSteb_12Parts11 - *****
steb_12Parts11Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\05_eb12_01_PartsStatusTable.uexp'
Head = Shinju(steb_12Parts11Path, 111)
Body = Shinju(steb_12Parts11Path, 1690)
ArmL = Shinju(steb_12Parts11Path, 3269)
ArmR = Shinju(steb_12Parts11Path, 4848)
Tail = Shinju(steb_12Parts11Path, 6427)

# ****** ShinjuStatusSteb_12Parts12 - *****
steb_12Parts12Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\06_eb12_01_PartsStatusTable.uexp'
Head = Shinju(steb_12Parts12Path, 111)
Body = Shinju(steb_12Parts12Path, 1690)
ArmL = Shinju(steb_12Parts12Path, 3269)
ArmR = Shinju(steb_12Parts12Path, 4848)
Tail = Shinju(steb_12Parts12Path, 6427)

# ****** ShinjuStatusSteb_12Parts13 - *****
steb_12Parts13Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\07_eb12_01_PartsStatusTable.uexp'
Head = Shinju(steb_12Parts13Path, 111)
Body = Shinju(steb_12Parts13Path, 1690)
ArmL = Shinju(steb_12Parts13Path, 3269)
ArmR = Shinju(steb_12Parts13Path, 4848)
Tail = Shinju(steb_12Parts13Path, 6427)

# ****** ShinjuStatusSteb_13Parts14 - *****
steb_13Parts14Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\01_eb13_01_PartsStatusTable.uexp'
Body = Shinju(steb_13Parts14Path, 111)
Altar_A = Shinju(steb_13Parts14Path, 1690)
Altar_B = Shinju(steb_13Parts14Path, 3269)
Altar_C = Shinju(steb_13Parts14Path, 4848)

# ****** ShinjuStatusSteb_13Parts15 - *****
steb_13Parts15Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\02_eb13_01_PartsStatusTable.uexp'
Body = Shinju(steb_13Parts15Path, 111)
Altar_A = Shinju(steb_13Parts15Path, 1690)
Altar_B = Shinju(steb_13Parts15Path, 3269)
Altar_C = Shinju(steb_13Parts15Path, 4848)

# ****** ShinjuStatusSteb_13Parts16 - *****
steb_13Parts16Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\03_eb13_01_PartsStatusTable.uexp'
Body = Shinju(steb_13Parts16Path, 111)
Altar_A = Shinju(steb_13Parts16Path, 1690)
Altar_B = Shinju(steb_13Parts16Path, 3269)
Altar_C = Shinju(steb_13Parts16Path, 4848)

# ****** ShinjuStatusSteb_13Parts17 - *****
steb_13Parts17Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\04_eb13_01_PartsStatusTable.uexp'
Body = Shinju(steb_13Parts17Path, 111)
Altar_A = Shinju(steb_13Parts17Path, 1690)
Altar_B = Shinju(steb_13Parts17Path, 3269)
Altar_C = Shinju(steb_13Parts17Path, 4848)

# ****** ShinjuStatusSteb_13Parts18 - *****
steb_13Parts18Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\05_eb13_01_PartsStatusTable.uexp'
Body = Shinju(steb_13Parts18Path, 111)
Altar_A = Shinju(steb_13Parts18Path, 1690)
Altar_B = Shinju(steb_13Parts18Path, 3269)
Altar_C = Shinju(steb_13Parts18Path, 4848)

# ****** ShinjuStatusSteb_13Parts19 - *****
steb_13Parts19Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\06_eb13_01_PartsStatusTable.uexp'
Body = Shinju(steb_13Parts19Path, 111)
Altar_A = Shinju(steb_13Parts19Path, 1690)
Altar_B = Shinju(steb_13Parts19Path, 3269)
Altar_C = Shinju(steb_13Parts19Path, 4848)

# ****** ShinjuStatusSteb_13Parts20 - *****
steb_13Parts20Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\07_eb13_01_PartsStatusTable.uexp'
Body = Shinju(steb_13Parts20Path, 111)
Altar_A = Shinju(steb_13Parts20Path, 1690)
Altar_B = Shinju(steb_13Parts20Path, 3269)
Altar_C = Shinju(steb_13Parts20Path, 4848)

# ****** ShinjuStatusSteb_14Parts21 - *****
steb_14Parts21Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\01_eb14_01_PartsStatusTable.uexp'
Head01_L = Shinju(steb_14Parts21Path, 111)
Head02_R = Shinju(steb_14Parts21Path, 1690)

# ****** ShinjuStatusSteb_14Parts22 - *****
steb_14Parts22Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\02_eb14_01_PartsStatusTable.uexp'
Head01_L = Shinju(steb_14Parts22Path, 111)
Head02_R = Shinju(steb_14Parts22Path, 1690)

# ****** ShinjuStatusSteb_14Parts23 - *****
steb_14Parts23Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\03_eb14_01_PartsStatusTable.uexp'
Head01_L = Shinju(steb_14Parts23Path, 111)
Head02_R = Shinju(steb_14Parts23Path, 1690)

# ****** ShinjuStatusSteb_14Parts24 - *****
steb_14Parts24Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\04_eb14_01_PartsStatusTable.uexp'
Head01_L = Shinju(steb_14Parts24Path, 111)
Head02_R = Shinju(steb_14Parts24Path, 1690)

# ****** ShinjuStatusSteb_14Parts25 - *****
steb_14Parts25Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\05_eb14_01_PartsStatusTable.uexp'
Head01_L = Shinju(steb_14Parts25Path, 111)
Head02_R = Shinju(steb_14Parts25Path, 1690)

# ****** ShinjuStatusSteb_14Parts26 - *****
steb_14Parts26Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\06_eb14_01_PartsStatusTable.uexp'
Head01_L = Shinju(steb_14Parts26Path, 111)
Head02_R = Shinju(steb_14Parts26Path, 1690)

# ****** ShinjuStatusSteb_14Parts27 - *****
steb_14Parts27Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\07_eb14_01_PartsStatusTable.uexp'
Head01_L = Shinju(steb_14Parts27Path, 111)
Head02_R = Shinju(steb_14Parts27Path, 1690)

# ****** ShinjuStatusSteb_15Parts28 - *****
steb_15Parts28Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\01_eb15_01_PartsStatusTable.uexp'
Head = Shinju(steb_15Parts28Path, 111)
Body = Shinju(steb_15Parts28Path, 1690)

# ****** ShinjuStatusSteb_15Parts29 - *****
steb_15Parts29Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\02_eb15_01_PartsStatusTable.uexp'
Head = Shinju(steb_15Parts29Path, 111)
Body = Shinju(steb_15Parts29Path, 1690)

# ****** ShinjuStatusSteb_15Parts30 - *****
steb_15Parts30Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\03_eb15_01_PartsStatusTable.uexp'
Head = Shinju(steb_15Parts30Path, 111)
Body = Shinju(steb_15Parts30Path, 1690)

# ****** ShinjuStatusSteb_15Parts31 - *****
steb_15Parts31Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\04_eb15_01_PartsStatusTable.uexp'
Head = Shinju(steb_15Parts31Path, 111)
Body = Shinju(steb_15Parts31Path, 1690)

# ****** ShinjuStatusSteb_15Parts32 - *****
steb_15Parts32Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\05_eb15_01_PartsStatusTable.uexp'
Head = Shinju(steb_15Parts32Path, 111)
Body = Shinju(steb_15Parts32Path, 1690)

# ****** ShinjuStatusSteb_15Parts33 - *****
steb_15Parts33Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\06_eb15_01_PartsStatusTable.uexp'
Head = Shinju(steb_15Parts33Path, 111)
Body = Shinju(steb_15Parts33Path, 1690)

# ****** ShinjuStatusSteb_15Parts34 - *****
steb_15Parts34Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\07_eb15_01_PartsStatusTable.uexp'
Head = Shinju(steb_15Parts34Path, 111)
Body = Shinju(steb_15Parts34Path, 1690)

# ****** ShinjuStatusSteb_16Parts35 - *****
steb_16Parts35Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\01_eb16_01_PartsTable.uexp'
Head = Shinju(steb_16Parts35Path, 111)
Body = Shinju(steb_16Parts35Path, 1690)
HandLB = Shinju(steb_16Parts35Path, 3269)
HandRB = Shinju(steb_16Parts35Path, 4848)

# ****** ShinjuStatusSteb_16Parts36 - *****
steb_16Parts36Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\02_eb16_01_PartsTable.uexp'
Head = Shinju(steb_16Parts36Path, 111)
Body = Shinju(steb_16Parts36Path, 1690)
HandLB = Shinju(steb_16Parts36Path, 3269)
HandRB = Shinju(steb_16Parts36Path, 4848)

# ****** ShinjuStatusSteb_16Parts37 - *****
steb_16Parts37Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\03_eb16_01_PartsTable.uexp'
Head = Shinju(steb_16Parts37Path, 111)
Body = Shinju(steb_16Parts37Path, 1690)
HandLB = Shinju(steb_16Parts37Path, 3269)
HandRB = Shinju(steb_16Parts37Path, 4848)

# ****** ShinjuStatusSteb_16Parts38 - *****
steb_16Parts38Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\04_eb16_01_PartsTable.uexp'
Head = Shinju(steb_16Parts38Path, 111)
Body = Shinju(steb_16Parts38Path, 1690)
HandLB = Shinju(steb_16Parts38Path, 3269)
HandRB = Shinju(steb_16Parts38Path, 4848)

# ****** ShinjuStatusSteb_16Parts39 - *****
steb_16Parts39Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\05_eb16_01_PartsTable.uexp'
Head = Shinju(steb_16Parts39Path, 111)
Body = Shinju(steb_16Parts39Path, 1690)
HandLB = Shinju(steb_16Parts39Path, 3269)
HandRB = Shinju(steb_16Parts39Path, 4848)

# ****** ShinjuStatusSteb_16Parts40 - *****
steb_16Parts40Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\06_eb16_01_PartsTable.uexp'
Head = Shinju(steb_16Parts40Path, 111)
Body = Shinju(steb_16Parts40Path, 1690)
HandLB = Shinju(steb_16Parts40Path, 3269)
HandRB = Shinju(steb_16Parts40Path, 4848)

# ****** ShinjuStatusSteb_16Parts41 - *****
steb_16Parts41Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\07_eb16_01_PartsTable.uexp'
Head = Shinju(steb_16Parts41Path, 111)
Body = Shinju(steb_16Parts41Path, 1690)
HandLB = Shinju(steb_16Parts41Path, 3269)
HandRB = Shinju(steb_16Parts41Path, 4848)

# ****** ShinjuStatusSteb_17Parts42 - *****
steb_17Parts42Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\01_eb17_01_PartsStatusTable.uexp'
Eye = Shinju(steb_17Parts42Path, 111)
Body = Shinju(steb_17Parts42Path, 1690)

# ****** ShinjuStatusSteb_17Parts43 - *****
steb_17Parts43Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\02_eb17_01_PartsStatusTable.uexp'
Eye = Shinju(steb_17Parts43Path, 111)
Body = Shinju(steb_17Parts43Path, 1690)

# ****** ShinjuStatusSteb_17Parts44 - *****
steb_17Parts44Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\03_eb17_01_PartsStatusTable.uexp'
Eye = Shinju(steb_17Parts44Path, 111)
Body = Shinju(steb_17Parts44Path, 1690)

# ****** ShinjuStatusSteb_17Parts45 - *****
steb_17Parts45Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\04_eb17_01_PartsStatusTable.uexp'
Eye = Shinju(steb_17Parts45Path, 111)
Body = Shinju(steb_17Parts45Path, 1690)

# ****** ShinjuStatusSteb_17Parts46 - *****
steb_17Parts46Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\05_eb17_01_PartsStatusTable.uexp'
Eye = Shinju(steb_17Parts46Path, 111)
Body = Shinju(steb_17Parts46Path, 1690)

# ****** ShinjuStatusSteb_17Parts47 - *****
steb_17Parts47Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\06_eb17_01_PartsStatusTable.uexp'
Eye = Shinju(steb_17Parts47Path, 111)
Body = Shinju(steb_17Parts47Path, 1690)

# ****** ShinjuStatusSteb_17Parts48 - *****
steb_17Parts48Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\07_eb17_01_PartsStatusTable.uexp'
Eye = Shinju(steb_17Parts48Path, 111)
Body = Shinju(steb_17Parts48Path, 1690)
#endregion


#region Parts Instance Creation Start
# ****** eb01_01_PartsStatusTable - *****
eb01_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb01_01_PartsStatusTable.uexp'
Head = Parts(eb01_01_PartsStatusTable_Path, 111)
Body = Parts(eb01_01_PartsStatusTable_Path, 1690)
ArmLB = Parts(eb01_01_PartsStatusTable_Path, 3269)
ArmRB = Parts(eb01_01_PartsStatusTable_Path, 4848)

# ****** eb01_02_PartsTable - *****
eb01_02_PartsTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb01_02_PartsTable.uexp'
Head = Parts(eb01_02_PartsTable_Path, 111)
Body = Parts(eb01_02_PartsTable_Path, 1690)
ArmLB = Parts(eb01_02_PartsTable_Path, 3269)
ArmRB = Parts(eb01_02_PartsTable_Path, 4848)

# ****** eb01_03_PartsTable - *****
eb01_03_PartsTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb01_03_PartsTable.uexp'
Head = Parts(eb01_03_PartsTable_Path, 111)
Body = Parts(eb01_03_PartsTable_Path, 1690)
ArmLB = Parts(eb01_03_PartsTable_Path, 3269)
ArmRB = Parts(eb01_03_PartsTable_Path, 4848)

# ****** eb03_01_PartsStatusTable - *****
eb03_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb03_01_PartsStatusTable.uexp'
None_part = Parts(eb03_01_PartsStatusTable_Path, 111)
Body = Parts(eb03_01_PartsStatusTable_Path, 1690)
ArmL = Parts(eb03_01_PartsStatusTable_Path, 3269)
ArmR = Parts(eb03_01_PartsStatusTable_Path, 4848)
Tail = Parts(eb03_01_PartsStatusTable_Path, 6427)

# ****** eb03_11_PartsStatusTable - *****
eb03_11_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb03_11_PartsStatusTable.uexp'
None_part = Parts(eb03_11_PartsStatusTable_Path, 111)
Body = Parts(eb03_11_PartsStatusTable_Path, 1690)
ArmL = Parts(eb03_11_PartsStatusTable_Path, 3269)
ArmR = Parts(eb03_11_PartsStatusTable_Path, 4848)
Tail = Parts(eb03_11_PartsStatusTable_Path, 6427)

# ****** eb07_01_PartsStatusTable - *****
eb07_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb07_01_PartsStatusTable.uexp'
Body = Parts(eb07_01_PartsStatusTable_Path, 111)
Shadow = Parts(eb07_01_PartsStatusTable_Path, 1690)
ShadowDummy1 = Parts(eb07_01_PartsStatusTable_Path, 3269)
ShadowDummy2 = Parts(eb07_01_PartsStatusTable_Path, 4848)
ShadowDummy3 = Parts(eb07_01_PartsStatusTable_Path, 6427)
ShadowDummy4 = Parts(eb07_01_PartsStatusTable_Path, 8006)
ShadowDummy5 = Parts(eb07_01_PartsStatusTable_Path, 9585)

# ****** eb07_11_PartsStatusTable - *****
eb07_11_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb07_11_PartsStatusTable.uexp'
Body = Parts(eb07_11_PartsStatusTable_Path, 111)
Shadow = Parts(eb07_11_PartsStatusTable_Path, 1690)
ShadowDummy1 = Parts(eb07_11_PartsStatusTable_Path, 3269)
ShadowDummy2 = Parts(eb07_11_PartsStatusTable_Path, 4848)
ShadowDummy3 = Parts(eb07_11_PartsStatusTable_Path, 6427)
ShadowDummy4 = Parts(eb07_11_PartsStatusTable_Path, 8006)
ShadowDummy5 = Parts(eb07_11_PartsStatusTable_Path, 9585)

# ****** eb10_01_PartsStatusTable - *****
eb10_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb10_01_PartsStatusTable.uexp'
Head = Parts(eb10_01_PartsStatusTable_Path, 111)
Body = Parts(eb10_01_PartsStatusTable_Path, 1690)
ArmL = Parts(eb10_01_PartsStatusTable_Path, 3269)
ArmTipL = Parts(eb10_01_PartsStatusTable_Path, 4848)
ArmR = Parts(eb10_01_PartsStatusTable_Path, 6427)
ArmTipR = Parts(eb10_01_PartsStatusTable_Path, 8006)
Neck = Parts(eb10_01_PartsStatusTable_Path, 9585)
Flower = Parts(eb10_01_PartsStatusTable_Path, 11164)

# ****** eb10_11_PartsStatusTable - *****
eb10_11_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb10_11_PartsStatusTable.uexp'
Head = Parts(eb10_11_PartsStatusTable_Path, 111)
Body = Parts(eb10_11_PartsStatusTable_Path, 1690)
ArmL = Parts(eb10_11_PartsStatusTable_Path, 3269)
ArmTipL = Parts(eb10_11_PartsStatusTable_Path, 4848)
ArmR = Parts(eb10_11_PartsStatusTable_Path, 6427)
ArmTipR = Parts(eb10_11_PartsStatusTable_Path, 8006)
Neck = Parts(eb10_11_PartsStatusTable_Path, 9585)
Flower = Parts(eb10_11_PartsStatusTable_Path, 11164)

# ****** eb11_01_PartsStatusTable - *****
eb11_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb11_01_PartsStatusTable.uexp'
Body = Parts(eb11_01_PartsStatusTable_Path, 111)
ArmL = Parts(eb11_01_PartsStatusTable_Path, 1690)
ArmR = Parts(eb11_01_PartsStatusTable_Path, 3269)
ArmL_Core01 = Parts(eb11_01_PartsStatusTable_Path, 4848)
ArmL_Core02 = Parts(eb11_01_PartsStatusTable_Path, 6427)
ArmR_Core01 = Parts(eb11_01_PartsStatusTable_Path, 8006)
ArmR_Core02 = Parts(eb11_01_PartsStatusTable_Path, 9585)

# ****** eb12_01_PartsStatusTable - *****
eb12_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb12_01_PartsStatusTable.uexp'
Head = Parts(eb12_01_PartsStatusTable_Path, 111)
Body = Parts(eb12_01_PartsStatusTable_Path, 1690)
ArmL = Parts(eb12_01_PartsStatusTable_Path, 3269)
ArmR = Parts(eb12_01_PartsStatusTable_Path, 4848)
Tail = Parts(eb12_01_PartsStatusTable_Path, 6427)

# ****** eb13_01_PartsStatusTable - *****
eb13_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb13_01_PartsStatusTable.uexp'
Body = Parts(eb13_01_PartsStatusTable_Path, 111)
Altar_A = Parts(eb13_01_PartsStatusTable_Path, 1690)
Altar_B = Parts(eb13_01_PartsStatusTable_Path, 3269)
Altar_C = Parts(eb13_01_PartsStatusTable_Path, 4848)

# ****** eb14_01_PartsStatusTable - *****
eb14_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb14_01_PartsStatusTable.uexp'
Head01_L = Parts(eb14_01_PartsStatusTable_Path, 111)
Head02_R = Parts(eb14_01_PartsStatusTable_Path, 1690)

# ****** eb15_01_PartsTable - *****
eb15_01_PartsTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb15_01_PartsTable.uexp'
Head = Parts(eb15_01_PartsTable_Path, 111)
Body = Parts(eb15_01_PartsTable_Path, 1690)

# ****** eb15_02_PartsTable - *****
eb15_02_PartsTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb15_02_PartsTable.uexp'
Head = Parts(eb15_02_PartsTable_Path, 111)

# ****** eb16_01_PartsTable - *****
eb16_01_PartsTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb16_01_PartsTable.uexp'
Head = Parts(eb16_01_PartsTable_Path, 111)
Body = Parts(eb16_01_PartsTable_Path, 1690)
HandLB = Parts(eb16_01_PartsTable_Path, 3269)
HandRB = Parts(eb16_01_PartsTable_Path, 4848)

# ****** eb17_01_PartsStatusTable - *****
eb17_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb17_01_PartsStatusTable.uexp'
Eye = Parts(eb17_01_PartsStatusTable_Path, 111)
Body = Parts(eb17_01_PartsStatusTable_Path, 1690)

# ****** eb21_01_PartsStatusTable - *****
eb21_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb21_01_PartsStatusTable.uexp'
Body = Parts(eb21_01_PartsStatusTable_Path, 111)
RouletteDeath_Actor01 = Parts(eb21_01_PartsStatusTable_Path, 1690)
RouletteDeath_Actor02 = Parts(eb21_01_PartsStatusTable_Path, 3269)
RouletteDeath_Actor03 = Parts(eb21_01_PartsStatusTable_Path, 4848)
RouletteDeath_Actor04 = Parts(eb21_01_PartsStatusTable_Path, 6427)

# ****** eb25_01_PartsStatusTable - *****
eb25_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb25_01_PartsStatusTable.uexp'
None_part = Parts(eb25_01_PartsStatusTable_Path, 111)
Body = Parts(eb25_01_PartsStatusTable_Path, 1690)
ArmL = Parts(eb25_01_PartsStatusTable_Path, 3269)
ArmR = Parts(eb25_01_PartsStatusTable_Path, 4848)
Tail = Parts(eb25_01_PartsStatusTable_Path, 6427)
None_part = Parts(eb25_01_PartsStatusTable_Path, 8006)
None_part = Parts(eb25_01_PartsStatusTable_Path, 9585)
None_part = Parts(eb25_01_PartsStatusTable_Path, 11164)

# ****** eb27_01_PartsStatusTable - *****
eb27_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb27_01_PartsStatusTable.uexp'
Body = Parts(eb27_01_PartsStatusTable_Path, 111)
ArmL = Parts(eb27_01_PartsStatusTable_Path, 1690)
ArmR = Parts(eb27_01_PartsStatusTable_Path, 3269)
SpiralMoon_Gimmick01 = Parts(eb27_01_PartsStatusTable_Path, 4848)
HellSouthernCross_Gimick01 = Parts(eb27_01_PartsStatusTable_Path, 6427)
HellSouthernCross_Gimick02 = Parts(eb27_01_PartsStatusTable_Path, 8006)
Gigaburn_Gimmick01 = Parts(eb27_01_PartsStatusTable_Path, 9585)
Gigaburn_Gimmick02 = Parts(eb27_01_PartsStatusTable_Path, 11164)
Gigaburn_Gimmick03 = Parts(eb27_01_PartsStatusTable_Path, 12743)

# ****** eb33_01_PartsStatusTable - *****
eb33_01_PartsStatusTable_Path = r'Game Files\Boss\Orig\uexp files\Parts\eb33_01_PartsStatusTable.uexp'
Head = Parts(eb33_01_PartsStatusTable_Path, 111)
Body = Parts(eb33_01_PartsStatusTable_Path, 1690)
#endregion


# default values in a dict
defaultDict = {}

defaultDict['hp'] = 2
defaultDict['atk'] = 1.5
defaultDict['def'] = 1
defaultDict['agi'] = 1.2
defaultDict['int'] = 1.5
defaultDict['spr'] = 1.5
defaultDict['luck'] = 1.2
defaultDict['defMag'] = 1
defaultDict['offMag'] = 1
defaultDict['exp'] = 1

# Create Dict for entering multipliers

multiDict = {}
bossDict = {}
shinjuDict = {}
partsDict = {}

onOffStart = True
while onOffStart:    
    defCheck = input('Would you like to use the "default" modifiers (the modifiers from the mod\'s premade release on the Nexus page)?\n' \
                    "The default modifiers are the following: HP: 2 (double HP), Atk: 1.5, Def: 1 (base value), Agi: 1.2, Int: 1.5, Spr: 1.5" \
                            ", Luck: 1.2, DefMag: 1, OffMag: 1, EXP: 1\n" \
                    'Input "y" if so, "n" to enter your own custom modifier values.\n\n' \
                                "Input: ")        
    if defCheck != 'y' and defCheck != 'n':
        print("\n***Please enter 'y' (no quotes) or 'n' as your input.\n")
    elif defCheck == 'y' or defCheck == 'n':
        onOffStart = False
        

# use default dict as values for everything if 'y'
if defCheck == 'y':
    for k, v in defaultDict.items():
        multiDict[k] = v
        bossDict[k] = v
        shinjuDict[k] = v
        partsDict[k] = v

elif defCheck == 'n':
    # TODO set up the layout for the command prompt inputs
    introMsg = "\nPlease enter what you would like the multipliers for each of the common enemies' stats to be: \n" \
                "NOTE: Enter '1' to keep the stat at its default value.\nWARNING: Entering '0' will set that stat to '0' for all enemies.\n"            
    print(introMsg)

    onOff = True
    while onOff:
        try:
            # *Caution: zero values will set that stat to 0
            multiDict['hp'] = float(input('Choose a multiplier for Enemy HP: '))
            multiDict['atk'] = float(input('Choose a multiplier for Enemy Atk: '))
            multiDict['def'] = float(input('Choose a multiplier for Enemy Def: '))
            multiDict['agi'] = float(input('Choose a multiplier for Enemy Agi: '))
            multiDict['int'] = float(input('Choose a multiplier for Enemy Int: '))
            multiDict['spr'] = float(input('Choose a multiplier for Enemy Spr: '))
            multiDict['luck'] = float(input('Choose a multiplier for Enemy Luck: '))
            multiDict['defMag'] = float(input('Choose a multiplier for Enemy defMag: '))
            multiDict['offMag'] = float(input('Choose a multiplier for Enemy offMag: '))
            multiDict['exp'] = float(input('Choose a multiplier for Enemy Exp: '))            
            print("\nThe multipliers you've selected for common enemies are:")
            print(str(multiDict) + "\n")
            while 1:
                confirm1 = input("Are you okay with these values? 'y' if so, 'n' to redo: \n")
                if confirm1 != 'y' and confirm1 != 'n':
                    print("\n***Please enter 'y' (no quotes) or 'n' as your input.")                    
                elif confirm1 == 'y' or confirm1 == 'n':                    
                    if confirm1 == 'y':                                        
                        onOff = False
                        break
                    elif confirm1 == 'n':                        
                        break
                        continue                            
        except ValueError:
            print('\nInput must be an integer (5, 6...) or float number (1.2, 2.3...)\n')

    onOffBoss = True
    while onOffBoss:
        msg2_Boss = input("\nPlease enter what you would like the multipliers for each of the boss's stats to be: \n" \
                "*TO USE THE SAME MULTIPLIERS AS THE ENEMIES, INPUT 'copy'. To enter your own modifiers for bosses, input 'n'.\n" \
                    "Input: ")
        if msg2_Boss != 'copy' and msg2_Boss != 'n':
            print("\n***Please enter 'copy' (no quotes) or 'n' as your input.\n")
        elif msg2_Boss == 'copy' or msg2_Boss == 'n':
            if msg2_Boss == 'copy':
                onOffBoss = False
            elif msg2_Boss == 'n':                                
                onOffBoss = False

    if msg2_Boss == 'copy':        
        for k, v in multiDict.items():        
            bossDict[k] = v
            shinjuDict[k] = v
            partsDict[k] = v
    elif msg2_Boss == 'n':
        onOff = True
        while onOff:
            try:
                bossDict['hp'] = float(input('Choose a multiplier for Boss HP: '))
                bossDict['atk'] = float(input('Choose a multiplier for Boss Atk: '))
                bossDict['def'] = float(input('Choose a multiplier for Boss Def: '))
                bossDict['agi'] = float(input('Choose a multiplier for Boss Agi: '))
                bossDict['int'] = float(input('Choose a multiplier for Boss Int: '))
                bossDict['spr'] = float(input('Choose a multiplier for Boss Spr: '))
                bossDict['luck'] = float(input('Choose a multiplier for Boss Luck: '))
                bossDict['defMag'] = float(input('Choose a multiplier for Boss defMag: '))
                bossDict['offMag'] = float(input('Choose a multiplier for Boss offMag: '))
                bossDict['exp'] = float(input('Choose a multiplier for Boss Exp: '))                
                print("\nThe multipliers you've selected for bosses are:")
                print(str(bossDict) + "\n")

                confirm1 = input("Are you okay with these values? 'y' if so, 'n' to redo: ")
                if confirm1 != 'y' and confirm1 != 'n':
                    print("\n***Please enter 'y' (no quotes) or 'n' as your input.\n")
                elif confirm1 == 'y' or confirm1 == 'n':
                    if confirm1 == 'y':                    
                        print("\n")
                        onOff = False
                    elif confirm1 == 'n':
                        print("\n")
                        continue


            except ValueError:
                print('Input must be an integer (5, 6...) or float number (1.2, 2.3...)')
        
        # For now, we're using the same multipliers for Boss adds as the main Boss stats. So do this no matter what
        # Copy values from bossDict to shinjuDict
        for k, v in bossDict.items():
            shinjuDict[k] = v
            partsDict[k] = v

print("The selected modifiers are: \n" \
        "Common Enemies: " + str(multiDict) + "\n" \
        "Bosses : " + str(bossDict) + "\n")

# DEBUG
print("\n********** DEBUG **********\n")
print(multiDict)
print(bossDict)
print(shinjuDict)
print(partsDict)

confirmEdit = input("If this is satisfactory, press 'enter' to continue. Otherwise, please close the console and restart.")
confirmEdit = None

print("\n")
print('Editing data files...\n')

editHexAll(multiDict)
editHexAll_Boss(bossDict)
editHexAll_Shinju(shinjuDict)
editHexAll_Parts(partsDict)

time.sleep(1)

print("Please check that the directory 'Custom_TofMania - 0.3_P' has new files created.\n" \
        "If the files existed before running this script, they should be updated now.\n")

closeVar = input("Press 'enter' to exit the console.")
closeVar = None
