from collections import defaultdict
import copy
from aoc_utils import timed

def main():
    input = []
    with open('test_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    space = defaultdict(lambda: '.')
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '#':
                space[(x,y,0)] = '#'

    for i in range(6):
        # display_space(space)
        space_count = defaultdict(lambda: 0)
        for pos in space.keys():
            add_to_neighbors(pos, space_count)
        new_space = defaultdict(lambda: '.')
        for pos in space_count.keys():
            if space[pos] == '#' and (space_count[pos] == 2 or space_count[pos] == 3):
                new_space[pos] = '#'
            elif space[pos] == '.' and space_count[pos] == 3:
                new_space[pos] = '#'
        space = new_space
    return len(space)

def display_space(space):
    space = copy.deepcopy(space)
    minx = maxx = list(space.keys())[0][0]
    miny = maxy = list(space.keys())[0][1]
    minz = maxz = list(space.keys())[0][2]
    for pos in space.keys():
        x, y, z = pos
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
        if z < minz:
            minz = z
        if z > maxz:
            maxz = z
    for z in range(minz, maxz+1):
        print(f'\nz={z}')
        for y in range(miny-1, maxy+1):
            if y != miny-1:
                print(f'y={y:2}:  ', end='')
            else:
                print('    x= ', end='')
            for x in range(minx, maxx+1):
                if y == miny-1:
                    print(f'{x:2} ', end='')
                else:
                    print(f' {space[(x,y,z)]} ', end='')
            print()

def add_to_neighbors(pos, new_space_count):
    x, y, z = pos
    for dx in range(-1,2):
        for dy in range(-1,2):
            for dz in range(-1,2):
                if dx != 0 or dy != 0 or dz != 0:
                    new_space_count[(x+dx, y+dy, z+dz)] += 1

def count_active(space):
    count = 0
    for val in space.values():
        if val == '#':
            count += 1
    return count

def part2(input):
    space = defaultdict(lambda: '.')
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '#':
                space[(x, y, 0, 0)] = '#'

    for i in range(6):
        space_count = defaultdict(lambda: 0)
        for pos in space.keys():
            add_to_neighbors_4D(pos, space, space_count)
        new_space = defaultdict(lambda: '.')
        for pos in space_count.keys():
            if space[pos] == '#' and (space_count[pos] == 2 or space_count[pos] == 3):
                new_space[pos] = '#'
            elif space[pos] == '.' and space_count[pos] == 3:
                new_space[pos] = '#'
        space = new_space
    return count_active(space)

def add_to_neighbors_4D(pos, space, new_space_count):
    x, y, z, w = pos
    for dx in range(-1,2):
        for dy in range(-1,2):
            for dz in range(-1,2):
                for dw in range(-1,2):
                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                        new_space_count[(x+dx, y+dy, z+dz, w+dw)] += 1
if __name__ == '__main__':
    main()