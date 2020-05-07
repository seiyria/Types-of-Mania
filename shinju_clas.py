import os


# Global list for iterating through and making edits to .uexp files
enemyInstList = []

finDirPath = 'final patch folder\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\ShinjuStatusTableList\\'


# TODO do we want to be able to update each class instance so we can check what its new value is?
class Enemy:
    # hpOffset is used as the base offset to calculate the other offsets
    def __init__(self, file_path, hpOffset):
        self.fileLocation = file_path
        
        self.attrOffsetDict = {}                
        
        # Append to global list for iterating
        enemyInstList.append(self)

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


# TODO add a conditional check to skip code if argument value (param?) is 0
def editHexAll(multiDict):
    
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

            for enemy in enemyInstList:                
                # Check each Enemy's fileLocation attr to see if it matches the current fullPath
                if enemy.fileLocation == fullPath:
                    for attr, offset in enemy.attrOffsetDict.items():
                        
                        # Original slice of four bytes in data that we will edit
                        fourBytesToEdit = byteData[offset:(offset + 4)]                    

                        # Convert those four bytes to an integer
                        numFromBytes = int.from_bytes(fourBytesToEdit, byteorder='little', signed=True)                    

                        newStatValue = round(numFromBytes * multiDict[attr])
                        # I don't think 99999 is the highest value allowed, so can maybe change in the future
                        if newStatValue > 99999:
                            newStatValue = 99999           

                        # new Stat value to 4 byte string
                        bytesToInsert = newStatValue.to_bytes(4, byteorder='little', signed=True)                    

                        # Insert new byte slice into mutable byte array
                        mutableBytes[offset:(offset + 4)] = bytesToInsert                    


            if 'CustomStatusTable.uexp' in file:
                outPath = finDirPath + file
                # TODO create nonexisting directory
                if not os.path.exists(finDirPath):
                    os.makedirs(finDirPath)
            elif '_eb11_' in file:                
                newPath11 = finDirPath + "eb_11Parts"
                if not os.path.exists(newPath11):
                    os.makedirs(newPath11)
                    outPath = newPath11 + "\\" + file
                else:
                    outPath = newPath11 + "\\" + file
            elif '_eb12_' in file:                
                newPath12 = finDirPath + "eb_12Parts"
                if not os.path.exists(newPath12):
                    os.makedirs(newPath12)
                    outPath = newPath12 + "\\" + file
                else:
                    outPath = newPath12 + "\\" + file
            elif '_eb13_' in file:                
                newPath13 = finDirPath + "eb_13Parts"
                if not os.path.exists(newPath13):
                    os.makedirs(newPath13)
                    outPath = newPath13 + "\\" + file
                else:
                    outPath = newPath13 + "\\" + file
            elif '_eb14_' in file:                
                newPath14 = finDirPath + "eb_14Parts"
                if not os.path.exists(newPath14):
                    os.makedirs(newPath14)
                    outPath = newPath14 + "\\" + file
                else:
                    outPath = newPath14 + "\\" + file  
            elif '_eb15_' in file:                
                newPath15 = finDirPath + "eb_15Parts"
                if not os.path.exists(newPath15):
                    os.makedirs(newPath15)
                    outPath = newPath15 + "\\" + file
                else:
                    outPath = newPath15 + "\\" + file
            elif '_eb16_' in file:                
                newPath16 = finDirPath + "eb_16Parts"
                if not os.path.exists(newPath16):
                    os.makedirs(newPath16)
                    outPath = newPath16 + "\\" + file
                else:
                    outPath = newPath16 + "\\" + file
            elif '_eb17_' in file:                
                newPath17 = finDirPath + "eb_17Parts"
                if not os.path.exists(newPath17):
                    os.makedirs(newPath17)
                    outPath = newPath17 + "\\" + file
                else:
                    outPath = newPath17 + "\\" + file              
            
            # Write files
            with open(outPath, 'wb') as f:
                f.write(mutableBytes)


# ********* Boss Instance Creation Start *********

# ShinjuStatusTableList

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb11_CustomStatusTable.uexp'
Land_amber = Enemy(stshinjuCustomPath, 140)
Land_amber = Enemy(stshinjuCustomPath, 1764)
Land_amber = Enemy(stshinjuCustomPath, 3388)
Land_amber = Enemy(stshinjuCustomPath, 5012)
Land_amber = Enemy(stshinjuCustomPath, 6636)
Land_amber = Enemy(stshinjuCustomPath, 8260)
Land_amber = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb12_CustomStatusTable.uexp'
Feegu_Mund = Enemy(stshinjuCustomPath, 140)
Feegu_Mund = Enemy(stshinjuCustomPath, 1764)
Feegu_Mund = Enemy(stshinjuCustomPath, 3388)
Feegu_Mund = Enemy(stshinjuCustomPath, 5012)
Feegu_Mund = Enemy(stshinjuCustomPath, 6636)
Feegu_Mund = Enemy(stshinjuCustomPath, 8260)
Feegu_Mund = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb13_CustomStatusTable.uexp'
Zan_Bie = Enemy(stshinjuCustomPath, 140)
Zan_Bie = Enemy(stshinjuCustomPath, 1764)
Zan_Bie = Enemy(stshinjuCustomPath, 3388)
Zan_Bie = Enemy(stshinjuCustomPath, 5012)
Zan_Bie = Enemy(stshinjuCustomPath, 6636)
Zan_Bie = Enemy(stshinjuCustomPath, 8260)
Zan_Bie = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb14_CustomStatusTable.uexp'
Dangard = Enemy(stshinjuCustomPath, 140)
Dangard = Enemy(stshinjuCustomPath, 1764)
Dangard = Enemy(stshinjuCustomPath, 3388)
Dangard = Enemy(stshinjuCustomPath, 5012)
Dangard = Enemy(stshinjuCustomPath, 6636)
Dangard = Enemy(stshinjuCustomPath, 8260)
Dangard = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb15_02_CustomStatusTable.uexp'
Mispolm = Enemy(stshinjuCustomPath, 140)
Mispolm = Enemy(stshinjuCustomPath, 1764)
Mispolm = Enemy(stshinjuCustomPath, 3388)
Mispolm = Enemy(stshinjuCustomPath, 5012)
Mispolm = Enemy(stshinjuCustomPath, 6636)
Mispolm = Enemy(stshinjuCustomPath, 8260)
Mispolm = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb15_CustomStatusTable.uexp'
Mispolm = Enemy(stshinjuCustomPath, 140)
Mispolm = Enemy(stshinjuCustomPath, 1764)
Mispolm = Enemy(stshinjuCustomPath, 3388)
Mispolm = Enemy(stshinjuCustomPath, 5012)
Mispolm = Enemy(stshinjuCustomPath, 6636)
Mispolm = Enemy(stshinjuCustomPath, 8260)
Mispolm = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb16_CustomStatusTable.uexp'
Doran = Enemy(stshinjuCustomPath, 140)
Doran = Enemy(stshinjuCustomPath, 1764)
Doran = Enemy(stshinjuCustomPath, 3388)
Doran = Enemy(stshinjuCustomPath, 5012)
Doran = Enemy(stshinjuCustomPath, 6636)
Doran = Enemy(stshinjuCustomPath, 8260)
Doran = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusStshinjuCustom - *****
stshinjuCustomPath = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb17_CustomStatusTable.uexp'
Light_Geizer = Enemy(stshinjuCustomPath, 140)
Light_Geizer = Enemy(stshinjuCustomPath, 1764)
Light_Geizer = Enemy(stshinjuCustomPath, 3388)
Light_Geizer = Enemy(stshinjuCustomPath, 5012)
Light_Geizer = Enemy(stshinjuCustomPath, 6636)
Light_Geizer = Enemy(stshinjuCustomPath, 8260)
Light_Geizer = Enemy(stshinjuCustomPath, 9884)

# ****** EnemyStatusSteb_11Parts0 - *****
steb_11Parts0Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\01_eb11_01_PartsStatusTable.uexp'
Body = Enemy(steb_11Parts0Path, 111)
ArmL = Enemy(steb_11Parts0Path, 1690)
ArmR = Enemy(steb_11Parts0Path, 3269)
ArmL_Core01 = Enemy(steb_11Parts0Path, 4848)
ArmL_Core02 = Enemy(steb_11Parts0Path, 6427)
ArmR_Core01 = Enemy(steb_11Parts0Path, 8006)
ArmR_Core02 = Enemy(steb_11Parts0Path, 9585)

# ****** EnemyStatusSteb_11Parts1 - *****
steb_11Parts1Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\02_eb11_01_PartsStatusTable.uexp'
Body = Enemy(steb_11Parts1Path, 111)
ArmL = Enemy(steb_11Parts1Path, 1690)
ArmR = Enemy(steb_11Parts1Path, 3269)
ArmL_Core01 = Enemy(steb_11Parts1Path, 4848)
ArmL_Core02 = Enemy(steb_11Parts1Path, 6427)
ArmR_Core01 = Enemy(steb_11Parts1Path, 8006)
ArmR_Core02 = Enemy(steb_11Parts1Path, 9585)

# ****** EnemyStatusSteb_11Parts2 - *****
steb_11Parts2Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\03_eb11_01_PartsStatusTable.uexp'
Body = Enemy(steb_11Parts2Path, 111)
ArmL = Enemy(steb_11Parts2Path, 1690)
ArmR = Enemy(steb_11Parts2Path, 3269)
ArmL_Core01 = Enemy(steb_11Parts2Path, 4848)
ArmL_Core02 = Enemy(steb_11Parts2Path, 6427)
ArmR_Core01 = Enemy(steb_11Parts2Path, 8006)
ArmR_Core02 = Enemy(steb_11Parts2Path, 9585)

# ****** EnemyStatusSteb_11Parts3 - *****
steb_11Parts3Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\04_eb11_01_PartsStatusTable.uexp'
Body = Enemy(steb_11Parts3Path, 111)
ArmL = Enemy(steb_11Parts3Path, 1690)
ArmR = Enemy(steb_11Parts3Path, 3269)
ArmL_Core01 = Enemy(steb_11Parts3Path, 4848)
ArmL_Core02 = Enemy(steb_11Parts3Path, 6427)
ArmR_Core01 = Enemy(steb_11Parts3Path, 8006)
ArmR_Core02 = Enemy(steb_11Parts3Path, 9585)

# ****** EnemyStatusSteb_11Parts4 - *****
steb_11Parts4Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\05_eb11_01_PartsStatusTable.uexp'
Body = Enemy(steb_11Parts4Path, 111)
ArmL = Enemy(steb_11Parts4Path, 1690)
ArmR = Enemy(steb_11Parts4Path, 3269)
ArmL_Core01 = Enemy(steb_11Parts4Path, 4848)
ArmL_Core02 = Enemy(steb_11Parts4Path, 6427)
ArmR_Core01 = Enemy(steb_11Parts4Path, 8006)
ArmR_Core02 = Enemy(steb_11Parts4Path, 9585)

# ****** EnemyStatusSteb_11Parts5 - *****
steb_11Parts5Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\06_eb11_01_PartsStatusTable.uexp'
Body = Enemy(steb_11Parts5Path, 111)
ArmL = Enemy(steb_11Parts5Path, 1690)
ArmR = Enemy(steb_11Parts5Path, 3269)
ArmL_Core01 = Enemy(steb_11Parts5Path, 4848)
ArmL_Core02 = Enemy(steb_11Parts5Path, 6427)
ArmR_Core01 = Enemy(steb_11Parts5Path, 8006)
ArmR_Core02 = Enemy(steb_11Parts5Path, 9585)

# ****** EnemyStatusSteb_11Parts6 - *****
steb_11Parts6Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_11Parts\07_eb11_01_PartsStatusTable.uexp'
Body = Enemy(steb_11Parts6Path, 111)
ArmL = Enemy(steb_11Parts6Path, 1690)
ArmR = Enemy(steb_11Parts6Path, 3269)
ArmL_Core01 = Enemy(steb_11Parts6Path, 4848)
ArmL_Core02 = Enemy(steb_11Parts6Path, 6427)
ArmR_Core01 = Enemy(steb_11Parts6Path, 8006)
ArmR_Core02 = Enemy(steb_11Parts6Path, 9585)

# ****** EnemyStatusSteb_12Parts7 - *****
steb_12Parts7Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\01_eb12_01_PartsStatusTable.uexp'
Head = Enemy(steb_12Parts7Path, 111)
Body = Enemy(steb_12Parts7Path, 1690)
ArmL = Enemy(steb_12Parts7Path, 3269)
ArmR = Enemy(steb_12Parts7Path, 4848)
Tail = Enemy(steb_12Parts7Path, 6427)

# ****** EnemyStatusSteb_12Parts8 - *****
steb_12Parts8Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\02_eb12_01_PartsStatusTable.uexp'
Head = Enemy(steb_12Parts8Path, 111)
Body = Enemy(steb_12Parts8Path, 1690)
ArmL = Enemy(steb_12Parts8Path, 3269)
ArmR = Enemy(steb_12Parts8Path, 4848)
Tail = Enemy(steb_12Parts8Path, 6427)

# ****** EnemyStatusSteb_12Parts9 - *****
steb_12Parts9Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\03_eb12_01_PartsStatusTable.uexp'
Head = Enemy(steb_12Parts9Path, 111)
Body = Enemy(steb_12Parts9Path, 1690)
ArmL = Enemy(steb_12Parts9Path, 3269)
ArmR = Enemy(steb_12Parts9Path, 4848)
Tail = Enemy(steb_12Parts9Path, 6427)

# ****** EnemyStatusSteb_12Parts10 - *****
steb_12Parts10Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\04_eb12_01_PartsStatusTable.uexp'
Head = Enemy(steb_12Parts10Path, 111)
Body = Enemy(steb_12Parts10Path, 1690)
ArmL = Enemy(steb_12Parts10Path, 3269)
ArmR = Enemy(steb_12Parts10Path, 4848)
Tail = Enemy(steb_12Parts10Path, 6427)

# ****** EnemyStatusSteb_12Parts11 - *****
steb_12Parts11Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\05_eb12_01_PartsStatusTable.uexp'
Head = Enemy(steb_12Parts11Path, 111)
Body = Enemy(steb_12Parts11Path, 1690)
ArmL = Enemy(steb_12Parts11Path, 3269)
ArmR = Enemy(steb_12Parts11Path, 4848)
Tail = Enemy(steb_12Parts11Path, 6427)

# ****** EnemyStatusSteb_12Parts12 - *****
steb_12Parts12Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\06_eb12_01_PartsStatusTable.uexp'
Head = Enemy(steb_12Parts12Path, 111)
Body = Enemy(steb_12Parts12Path, 1690)
ArmL = Enemy(steb_12Parts12Path, 3269)
ArmR = Enemy(steb_12Parts12Path, 4848)
Tail = Enemy(steb_12Parts12Path, 6427)

# ****** EnemyStatusSteb_12Parts13 - *****
steb_12Parts13Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_12Parts\07_eb12_01_PartsStatusTable.uexp'
Head = Enemy(steb_12Parts13Path, 111)
Body = Enemy(steb_12Parts13Path, 1690)
ArmL = Enemy(steb_12Parts13Path, 3269)
ArmR = Enemy(steb_12Parts13Path, 4848)
Tail = Enemy(steb_12Parts13Path, 6427)

# ****** EnemyStatusSteb_13Parts14 - *****
steb_13Parts14Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\01_eb13_01_PartsStatusTable.uexp'
Body = Enemy(steb_13Parts14Path, 111)
Altar_A = Enemy(steb_13Parts14Path, 1690)
Altar_B = Enemy(steb_13Parts14Path, 3269)
Altar_C = Enemy(steb_13Parts14Path, 4848)

# ****** EnemyStatusSteb_13Parts15 - *****
steb_13Parts15Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\02_eb13_01_PartsStatusTable.uexp'
Body = Enemy(steb_13Parts15Path, 111)
Altar_A = Enemy(steb_13Parts15Path, 1690)
Altar_B = Enemy(steb_13Parts15Path, 3269)
Altar_C = Enemy(steb_13Parts15Path, 4848)

# ****** EnemyStatusSteb_13Parts16 - *****
steb_13Parts16Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\03_eb13_01_PartsStatusTable.uexp'
Body = Enemy(steb_13Parts16Path, 111)
Altar_A = Enemy(steb_13Parts16Path, 1690)
Altar_B = Enemy(steb_13Parts16Path, 3269)
Altar_C = Enemy(steb_13Parts16Path, 4848)

# ****** EnemyStatusSteb_13Parts17 - *****
steb_13Parts17Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\04_eb13_01_PartsStatusTable.uexp'
Body = Enemy(steb_13Parts17Path, 111)
Altar_A = Enemy(steb_13Parts17Path, 1690)
Altar_B = Enemy(steb_13Parts17Path, 3269)
Altar_C = Enemy(steb_13Parts17Path, 4848)

# ****** EnemyStatusSteb_13Parts18 - *****
steb_13Parts18Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\05_eb13_01_PartsStatusTable.uexp'
Body = Enemy(steb_13Parts18Path, 111)
Altar_A = Enemy(steb_13Parts18Path, 1690)
Altar_B = Enemy(steb_13Parts18Path, 3269)
Altar_C = Enemy(steb_13Parts18Path, 4848)

# ****** EnemyStatusSteb_13Parts19 - *****
steb_13Parts19Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\06_eb13_01_PartsStatusTable.uexp'
Body = Enemy(steb_13Parts19Path, 111)
Altar_A = Enemy(steb_13Parts19Path, 1690)
Altar_B = Enemy(steb_13Parts19Path, 3269)
Altar_C = Enemy(steb_13Parts19Path, 4848)

# ****** EnemyStatusSteb_13Parts20 - *****
steb_13Parts20Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_13Parts\07_eb13_01_PartsStatusTable.uexp'
Body = Enemy(steb_13Parts20Path, 111)
Altar_A = Enemy(steb_13Parts20Path, 1690)
Altar_B = Enemy(steb_13Parts20Path, 3269)
Altar_C = Enemy(steb_13Parts20Path, 4848)

# ****** EnemyStatusSteb_14Parts21 - *****
steb_14Parts21Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\01_eb14_01_PartsStatusTable.uexp'
Head01_L = Enemy(steb_14Parts21Path, 111)
Head02_R = Enemy(steb_14Parts21Path, 1690)

# ****** EnemyStatusSteb_14Parts22 - *****
steb_14Parts22Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\02_eb14_01_PartsStatusTable.uexp'
Head01_L = Enemy(steb_14Parts22Path, 111)
Head02_R = Enemy(steb_14Parts22Path, 1690)

# ****** EnemyStatusSteb_14Parts23 - *****
steb_14Parts23Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\03_eb14_01_PartsStatusTable.uexp'
Head01_L = Enemy(steb_14Parts23Path, 111)
Head02_R = Enemy(steb_14Parts23Path, 1690)

# ****** EnemyStatusSteb_14Parts24 - *****
steb_14Parts24Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\04_eb14_01_PartsStatusTable.uexp'
Head01_L = Enemy(steb_14Parts24Path, 111)
Head02_R = Enemy(steb_14Parts24Path, 1690)

# ****** EnemyStatusSteb_14Parts25 - *****
steb_14Parts25Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\05_eb14_01_PartsStatusTable.uexp'
Head01_L = Enemy(steb_14Parts25Path, 111)
Head02_R = Enemy(steb_14Parts25Path, 1690)

# ****** EnemyStatusSteb_14Parts26 - *****
steb_14Parts26Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\06_eb14_01_PartsStatusTable.uexp'
Head01_L = Enemy(steb_14Parts26Path, 111)
Head02_R = Enemy(steb_14Parts26Path, 1690)

# ****** EnemyStatusSteb_14Parts27 - *****
steb_14Parts27Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_14Parts\07_eb14_01_PartsStatusTable.uexp'
Head01_L = Enemy(steb_14Parts27Path, 111)
Head02_R = Enemy(steb_14Parts27Path, 1690)

# ****** EnemyStatusSteb_15Parts28 - *****
steb_15Parts28Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\01_eb15_01_PartsStatusTable.uexp'
Head = Enemy(steb_15Parts28Path, 111)
Body = Enemy(steb_15Parts28Path, 1690)

# ****** EnemyStatusSteb_15Parts29 - *****
steb_15Parts29Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\02_eb15_01_PartsStatusTable.uexp'
Head = Enemy(steb_15Parts29Path, 111)
Body = Enemy(steb_15Parts29Path, 1690)

# ****** EnemyStatusSteb_15Parts30 - *****
steb_15Parts30Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\03_eb15_01_PartsStatusTable.uexp'
Head = Enemy(steb_15Parts30Path, 111)
Body = Enemy(steb_15Parts30Path, 1690)

# ****** EnemyStatusSteb_15Parts31 - *****
steb_15Parts31Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\04_eb15_01_PartsStatusTable.uexp'
Head = Enemy(steb_15Parts31Path, 111)
Body = Enemy(steb_15Parts31Path, 1690)

# ****** EnemyStatusSteb_15Parts32 - *****
steb_15Parts32Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\05_eb15_01_PartsStatusTable.uexp'
Head = Enemy(steb_15Parts32Path, 111)
Body = Enemy(steb_15Parts32Path, 1690)

# ****** EnemyStatusSteb_15Parts33 - *****
steb_15Parts33Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\06_eb15_01_PartsStatusTable.uexp'
Head = Enemy(steb_15Parts33Path, 111)
Body = Enemy(steb_15Parts33Path, 1690)

# ****** EnemyStatusSteb_15Parts34 - *****
steb_15Parts34Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_15Parts\07_eb15_01_PartsStatusTable.uexp'
Head = Enemy(steb_15Parts34Path, 111)
Body = Enemy(steb_15Parts34Path, 1690)

# ****** EnemyStatusSteb_16Parts35 - *****
steb_16Parts35Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\01_eb16_01_PartsTable.uexp'
Head = Enemy(steb_16Parts35Path, 111)
Body = Enemy(steb_16Parts35Path, 1690)
HandLB = Enemy(steb_16Parts35Path, 3269)
HandRB = Enemy(steb_16Parts35Path, 4848)

# ****** EnemyStatusSteb_16Parts36 - *****
steb_16Parts36Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\02_eb16_01_PartsTable.uexp'
Head = Enemy(steb_16Parts36Path, 111)
Body = Enemy(steb_16Parts36Path, 1690)
HandLB = Enemy(steb_16Parts36Path, 3269)
HandRB = Enemy(steb_16Parts36Path, 4848)

# ****** EnemyStatusSteb_16Parts37 - *****
steb_16Parts37Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\03_eb16_01_PartsTable.uexp'
Head = Enemy(steb_16Parts37Path, 111)
Body = Enemy(steb_16Parts37Path, 1690)
HandLB = Enemy(steb_16Parts37Path, 3269)
HandRB = Enemy(steb_16Parts37Path, 4848)

# ****** EnemyStatusSteb_16Parts38 - *****
steb_16Parts38Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\04_eb16_01_PartsTable.uexp'
Head = Enemy(steb_16Parts38Path, 111)
Body = Enemy(steb_16Parts38Path, 1690)
HandLB = Enemy(steb_16Parts38Path, 3269)
HandRB = Enemy(steb_16Parts38Path, 4848)

# ****** EnemyStatusSteb_16Parts39 - *****
steb_16Parts39Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\05_eb16_01_PartsTable.uexp'
Head = Enemy(steb_16Parts39Path, 111)
Body = Enemy(steb_16Parts39Path, 1690)
HandLB = Enemy(steb_16Parts39Path, 3269)
HandRB = Enemy(steb_16Parts39Path, 4848)

# ****** EnemyStatusSteb_16Parts40 - *****
steb_16Parts40Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\06_eb16_01_PartsTable.uexp'
Head = Enemy(steb_16Parts40Path, 111)
Body = Enemy(steb_16Parts40Path, 1690)
HandLB = Enemy(steb_16Parts40Path, 3269)
HandRB = Enemy(steb_16Parts40Path, 4848)

# ****** EnemyStatusSteb_16Parts41 - *****
steb_16Parts41Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_16Parts\07_eb16_01_PartsTable.uexp'
Head = Enemy(steb_16Parts41Path, 111)
Body = Enemy(steb_16Parts41Path, 1690)
HandLB = Enemy(steb_16Parts41Path, 3269)
HandRB = Enemy(steb_16Parts41Path, 4848)

# ****** EnemyStatusSteb_17Parts42 - *****
steb_17Parts42Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\01_eb17_01_PartsStatusTable.uexp'
Eye = Enemy(steb_17Parts42Path, 111)
Body = Enemy(steb_17Parts42Path, 1690)

# ****** EnemyStatusSteb_17Parts43 - *****
steb_17Parts43Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\02_eb17_01_PartsStatusTable.uexp'
Eye = Enemy(steb_17Parts43Path, 111)
Body = Enemy(steb_17Parts43Path, 1690)

# ****** EnemyStatusSteb_17Parts44 - *****
steb_17Parts44Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\03_eb17_01_PartsStatusTable.uexp'
Eye = Enemy(steb_17Parts44Path, 111)
Body = Enemy(steb_17Parts44Path, 1690)

# ****** EnemyStatusSteb_17Parts45 - *****
steb_17Parts45Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\04_eb17_01_PartsStatusTable.uexp'
Eye = Enemy(steb_17Parts45Path, 111)
Body = Enemy(steb_17Parts45Path, 1690)

# ****** EnemyStatusSteb_17Parts46 - *****
steb_17Parts46Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\05_eb17_01_PartsStatusTable.uexp'
Eye = Enemy(steb_17Parts46Path, 111)
Body = Enemy(steb_17Parts46Path, 1690)

# ****** EnemyStatusSteb_17Parts47 - *****
steb_17Parts47Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\06_eb17_01_PartsStatusTable.uexp'
Eye = Enemy(steb_17Parts47Path, 111)
Body = Enemy(steb_17Parts47Path, 1690)

# ****** EnemyStatusSteb_17Parts48 - *****
steb_17Parts48Path = r'Game Files\Boss\Orig\uexp files\ShinjuStatusTableList\eb_17Parts\07_eb17_01_PartsStatusTable.uexp'
Eye = Enemy(steb_17Parts48Path, 111)
Body = Enemy(steb_17Parts48Path, 1690)


# Create Dict for entering multipliers

multiDict = {}

# *Caution: zero values will set that stat to 0
multiDict['hp'] = 2
multiDict['atk'] = 1.5
multiDict['def'] = 1.2
multiDict['agi'] = 1.2
multiDict['int'] = 1.5
multiDict['spr'] = 1.5
multiDict['luck'] = 1.2
multiDict['defMag'] = 1.2
multiDict['offMag'] = 1.2
multiDict['exp'] = 1

editHexAll(multiDict)
