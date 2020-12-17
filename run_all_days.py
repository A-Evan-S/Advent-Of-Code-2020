import importlib
import os
from aoc_utils import time_execution

def main():
    _, runtime = time_execution(run_days, None)
    print(f'\nTotal Runtime: {runtime}')

def run_days(_): # this feels wrong
    cwd = os.getcwd()
    for day_num in range(1,26):
        print(f'             --- Day {day_num:2} ---')
        try:
            os.chdir(f'{cwd}/Day_{day_num:02}')
            module = importlib.import_module(f'Day_{day_num:02}.day{day_num}')
            module.main()
        except:
            print('incomplete')

if __name__ == '__main__':
    main()
