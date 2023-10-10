import os
import sys
import pathlib

demo_abs_path = pathlib.PurePath(os.path.abspath(__file__))
demo_dir_path = str(demo_abs_path.parents[1])
sys.path.insert(0,demo_dir_path)

from beta.config import Configuration as BetaConfig
from config import Configuration


def get_alpha():
    print("Demo from alpha")
    print((Configuration.AUTHOR, Configuration.TITLE))
    print(BetaConfig.EMAIL)
    
if __name__ == '__main__':
    get_alpha()