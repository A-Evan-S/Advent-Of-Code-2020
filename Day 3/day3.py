from functools import reduce

def main():
    input = []
    with open('day3_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

def part1(input):
    return count_trees(input, (3, 1))

def part2(input):
    angles = [(5,1),(1,1),(3,1),(7,1),(1,2)]
    return reduce(lambda x, y : count_trees(input, y) * x, angles, 1)

def count_trees(input, angle):
    right, down = angle
    trees = 0
    row = col = 0
    while row < len(input):
        if input[row][col%len(input[0])] == '#':
            trees+=1
        row += down
        col += right
    return trees

if __name__ == '__main__':
    main()