import sys, os, pathlib, shlex, shutil
from time import sleep

class Compiler:
    def __init__(self):
        os.system('cls')
        print("CustomScript Compiler\nM1dnight (c) 2023\nv0.2\n---------\n")
        print("> checking for arg")
        self.runInitialCheck()
        self.filePath = sys.argv[1]
        self.file = open(self.filePath, "r")
        self.beginParsingFile(self.file)
        # self.compileSB3Project()

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
                    if lineSplit[0][0] == "#": pass
                    else: self.fileLinesSplit.append(lineSplit)
                except Exception as e: del self.fileLines[i]
                    # print(f'+ > line {i+1}: parse failed, reason: {e}')
            else: pass
            i=i+1
        print(*self.fileLinesSplit, sep='\n')

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

    def compileSB3Project(self):
        print("> intializing compile to .sb3")
        shutil.make_archive(sys.argv[2], 'zip', pathlib.Path(sys.argv[1]).parent.absolute())
        p=pathlib.Path(pathlib.Path(pathlib.Path(sys.argv[1]).parent.absolute().parts[-1]).parts[-1]+".zip")
        p.rename(p.with_suffix('.sb3'))
        print("> successfully compiled")

Compiler()
