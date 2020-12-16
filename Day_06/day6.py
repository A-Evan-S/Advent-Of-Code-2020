from aoc_utils import timed

def main():
    with open('day6_input.txt') as f:
        input = f.read()
    input = input.split('\n\n')
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    count = 0
    for group in input:
        for i in range(ord('a'),ord('z')+1):
            if chr(i) in group:
                count += 1
    return count

def part2(input):
    count = 0
    for group in input:
        group_size = 1 + group.count('\n')
        for i in range(ord('a'), ord('z') + 1):
            if group.count(chr(i)) == group_size:
                count += 1
    return count

if __name__ == '__main__':
    main()