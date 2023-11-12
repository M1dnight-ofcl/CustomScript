import shutil, pathlib, os
def compileSB3Project(args):
    print("> intializing compile to .sb3")
    shutil.make_archive(args[1], 'zip', pathlib.Path(args[0]).parent.absolute())
    p=pathlib.Path(pathlib.Path(pathlib.Path(args[0]).parent.absolute().parts[-1]).parts[-1]+".zip")
    try: print('+ > creating file'); p.rename(p.with_suffix('.sb3'))
    except: print('+ - > file exists; overwriting file...'); os.remove(pathlib.Path(pathlib.Path(args[0]).parent.absolute().parts[-1]).parts[-1]+".sb3"); p.rename(p.with_suffix('.sb3'))
    print("= > successfully compiled")