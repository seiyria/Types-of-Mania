import os


# Global list for iterating through and making edits to .uexp files
enemyInstList = []

# path we want the edited files to output to for UnrealPak.exe
finDirPath = 'final patch folder\\Trials of Mana\\Content\\Game00\\Data\\Csv\\CharaData\\'


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
    rootdir = r'Game Files\Boss\Orig\uexp files'

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


            if file == 'BossStatusTable.uexp':
                outPath = finDirPath + file
                # TODO create nonexisting directory
                if not os.path.exists(finDirPath):
                    os.makedirs(finDirPath)            
            
            with open(outPath, 'wb') as f:
                f.write(mutableBytes)


# ********* Boss Instance Creation Start *********

# Charadata
# ****** EnemyStatusStbossSt - *****

stbossStPath = r'Game Files\Boss\Orig\uexp files\Charadata\BossStatusTable.uexp'

FullmetalHugger = Enemy(stbossStPath, 140)
MachineGolemR = Enemy(stbossStPath, 1764)
Jewel_EaterR = Enemy(stbossStPath, 3388)
Zhenker = Enemy(stbossStPath, 5012)
Genoa = Enemy(stbossStPath, 6636)
Bill = Enemy(stbossStPath, 8260)
Ben = Enemy(stbossStPath, 9884)
Bill_and_Ben = Enemy(stbossStPath, 11508)
Gorva = Enemy(stbossStPath, 13132)
MachineGolemS = Enemy(stbossStPath, 14756)
Beast_Ruger = Enemy(stbossStPath, 16380)
Guilder_Vine = Enemy(stbossStPath, 18004)
Land_amber = Enemy(stbossStPath, 19628)
Feegu_Mund = Enemy(stbossStPath, 21252)
Zan_Bie = Enemy(stbossStPath, 22876)
Dangard = Enemy(stbossStPath, 24500)
Mispolm = Enemy(stbossStPath, 26124)
Doran = Enemy(stbossStPath, 27748)
Light_Geizer = Enemy(stbossStPath, 29372)
Sablehor = Enemy(stbossStPath, 30996)
BlackKnight = Enemy(stbossStPath, 32620)
CrimsonWizard = Enemy(stbossStPath, 34244)
CrimsonWizardEvent = Enemy(stbossStPath, 35868)
Man_eating_death = Enemy(stbossStPath, 37492)
Fallen_saint = Enemy(stbossStPath, 39116)
Earl_of_evil_eye = Enemy(stbossStPath, 40740)
JewelryBeast = Enemy(stbossStPath, 42364)
HugeDragon = Enemy(stbossStPath, 43988)
DarkRich = Enemy(stbossStPath, 45612)
ArchDemon = Enemy(stbossStPath, 47236)
BlackRabi = Enemy(stbossStPath, 48860)
MiniBlackRabi = Enemy(stbossStPath, 50484)
Bruiser = Enemy(stbossStPath, 52108)
Karl = Enemy(stbossStPath, 53732)
Bill = Enemy(stbossStPath, 55356)
Ben = Enemy(stbossStPath, 56980)
Bill_and_Ben = Enemy(stbossStPath, 58604)
Gorva = Enemy(stbossStPath, 60228)
FullmetalHugger = Enemy(stbossStPath, 61852)
Man_eating_death_Avatar = Enemy(stbossStPath, 63476)
Jewel_Eater = Enemy(stbossStPath, 65100)
Zhenker = Enemy(stbossStPath, 66724)
Genoa = Enemy(stbossStPath, 68348)
Guilder_Vine = Enemy(stbossStPath, 69972)
Anise = Enemy(stbossStPath, 71596)
AniseDragon = Enemy(stbossStPath, 73220)
Sablehor_BlueMan = Enemy(stbossStPath, 74844)
Sablehor_PurpleMan = Enemy(stbossStPath, 76468)
ManaStone_Earth = Enemy(stbossStPath, 78092)
ManaStone_Water = Enemy(stbossStPath, 79716)
ManaStone_Fire = Enemy(stbossStPath, 81340)
ManaStone_Wind = Enemy(stbossStPath, 82964)
Anise_Avatar = Enemy(stbossStPath, 84588)
ManaStone_Black = Enemy(stbossStPath, 86212)
Mispolm_Ivy = Enemy(stbossStPath, 87836)
Roki = Enemy(stbossStPath, 89460)
BeastKing = Enemy(stbossStPath, 91084)
Crystal = Enemy(stbossStPath, 92708)
ArchDemon_ArmL = Enemy(stbossStPath, 94332)
ArchDemon_ArmR = Enemy(stbossStPath, 95956)
FullmetalHugger = Enemy(stbossStPath, 97580)
Zhenker = Enemy(stbossStPath, 99204)
Genoa = Enemy(stbossStPath, 100828)


# ShinjuStatusTableList



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
