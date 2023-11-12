import sys, os, pathlib, shlex, shutil
from time import sleep
from .scripts import compileToSB3 as c
import hashlib

class Compiler:
    def __init__(self):
        os.system('cls')
        print("CustomScript Compiler\nM1dnight (c) 2023\nv0.2\n---------\n")
        self.runInitialCheck()
        print('> initializing compiler\n')
        self.filePath = sys.argv[1]
        self.file = open(self.filePath, "r")
        self.beginParsingFile(self.file)
        c.compileSB3Project([sys.argv[1], sys.argv[2]])

    def beginParsingFile(self, file):
        print("> initiliazing file parse")
        self.fileContents = file.read()
        self.fileLines = self.fileContents.split('\n')
        # print(self.fileLines)
        i=0
        self.fileLinesSplit=[]
        print('+ > running file check scan; status', end=": ")
        for lineContents in self.fileLines:
            lineSplit = shlex.split(lineContents)
            if not len(lineSplit) < 1:
                try: # print(f'+ > line {i+1}: {lineSplit}')
                    ctkn=0
                    for token in lineSplit: lineSplit[ctkn]=token.translate({ord('('): None, ord(')'): None}); ctkn=ctkn+1
                    if lineSplit[0][0] == "#": pass
                    else: self.fileLinesSplit.append(lineSplit)
                except Exception as e: del self.fileLines[i]; # print(f'+ > line {i+1}: parse failed, reason: {e}')
            else: pass
            i=i+1
        print("✓")
        # print(*self.fileLinesSplit, sep='\n')
        print('+ > begining file compile to json; status', end=": ")
        for lineContentsSplit in self.fileLinesSplit :
            if lineContentsSplit[0] == "when":
                pass
        print("✓")
        print('= > file parsed successfully\n')

    def runInitialCheck(self):
        print("> checking for arg", end=": ")
        if len(sys.argv)-1 < 2: print('🞪'); raise ValueError('argument missing')
        print("✓")
        file = sys.argv[1]
        print(f'> got file arg "{file}"')
        flExt=str(pathlib.Path(file).suffix)
        print('> checking filetype', end=": ")
        if not flExt.lower() in [".cs1"]: print(f'🞪'); raise TypeError(f'inavlid file type ("{flExt}")')
        print("✓")
        print('> checking file existance', end=": ")
        if not os.path.exists(file):  print('🞪'); raise FileNotFoundError('file ("{file}") does not exist')
        print("✓")

    def generateAssetId(self,fileContents):
        return hashlib.md5(fileContents.encode()).hexdigest()

