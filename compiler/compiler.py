import sys, os, pathlib, shlex, shutil
from time import sleep
from compileToSB3 import compileSB3Project

class Compiler:
    def __init__(self):
        os.system('cls')
        print("CustomScript Compiler\nM1dnight (c) 2023\nv0.2\n---------\n")
        print("> checking for arg")
        self.runInitialCheck()
        self.filePath = sys.argv[1]
        self.file = open(self.filePath, "r")
        self.beginParsingFile(self.file)
        compileSB3Project([sys.argv[1], sys.argv[2]])

    def beginParsingFile(self, file):
        print("> initiliazing file parse")
        self.fileContents = file.read()
        self.fileLines = self.fileContents.split('\n')
        # print(self.fileLines)
        i=0
        self.fileLinesSplit=[]
        for lineContents in self.fileLines:
            lineSplit = shlex.split(lineContents)
            if not len(lineSplit) < 1:
                try:
                    # print(f'+ > line {i+1}: {lineSplit}')
                    ctkn=0
                    for token in lineSplit:
                        lineSplit[ctkn]=token.translate({ord('('): None, ord(')'): None})
                        ctkn=ctkn+1
                    if lineSplit[0][0] == "#": pass
                    else: self.fileLinesSplit.append(lineSplit)
                except Exception as e: del self.fileLines[i]
                    # print(f'+ > line {i+1}: parse failed, reason: {e}')
            else: pass
            i=i+1
        print(*self.fileLinesSplit, sep='\n')
        for lineContentsSplit in self.fileLinesSplit :
            if lineContentsSplit[0] == "when":
                pass

    def runInitialCheck(self):
        if len(sys.argv)-1 < 2: raise AttributeError("Please specify A file to compile")
        file = sys.argv[1]
        print(f'> got file arg "{file}"')
        print('> initializing compiler')
        flExt=str(pathlib.Path(file).suffix)
        print('> checking filetype')
        if not flExt.lower() in [".cs1"]:
            raise TypeError(f"File type ({flExt}) invalid")
        print('> checking file existance')
        if not os.path.exists(file):  raise FileNotFoundError(f"File {pathlib.Path(file).absolute()} does not exist")

Compiler()
