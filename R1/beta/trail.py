import os
import sys
import pathlib

trail_abs_path = pathlib.PurePath(os.path.abspath(__file__))
trail_dir_path = str(trail_abs_path.parents[1])
sys.path.insert(0, trail_dir_path)

from alpha.config import Configuration as AlphaConfig


def get_beta():
    print('This is Beta')
    print(AlphaConfig.AUTHOR)
    
if __name__ == '__main__':
    get_beta()