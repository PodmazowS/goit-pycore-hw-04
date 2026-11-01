from pathlib import Path
from colorama import Fore

def get_dir_tree(path: Path, space = ""):

    p = Path(path)

    #Recursively iterating through each element in the tree.
    for el in p.iterdir():
        if el.is_dir():
            print(Fore.BLUE + f"{space}{el.name}/")
            get_dir_tree(el, space + "   ")
            
        else:
            print(Fore.GREEN + f"{space}{el.name}")
            