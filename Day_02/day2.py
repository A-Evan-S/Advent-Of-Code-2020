from aoc_utils import timed

def main():
    input = []
    with open('day2_input.txt') as f:
        for line in f:
            input.append(line)
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    count = 0
    for line in input:
        range, char, password = line.split()
        range_min, range_max = range.split('-')
        range_min = int(range_min)
        range_max = int(range_max)
        char = char[0]
        char_count = 0
        for letter in password:
            if letter == char:
                char_count+=1
        if range_min<=char_count<=range_max:
            count+=1
    return count

def part2(input):
    count = 0
    for line in input:
        range, char, password = line.split()
        range_min, range_max = range.split('-')
        range_min = int(range_min)
        range_max = int(range_max)
        char = char[0]
        if (password[range_min-1] == char) != (password[range_max-1] == char):
            count += 1
    return count

if __name__ == '__main__':
    main()