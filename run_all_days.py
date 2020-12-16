import importlib
import os

def main():
    for day_num in range(1,26):
        print(f'             --- Day {day_num:2} ---')
        try:
            os.chdir(f'C:/Users/aevan/PycharmProjects/Advent Of Code 2020/Day_{day_num:02}')
            module = importlib.import_module(f'Day_{day_num:02}.day{day_num}')
            module.main()
        except:
            print('incomplete')


if __name__ == '__main__':
    main()