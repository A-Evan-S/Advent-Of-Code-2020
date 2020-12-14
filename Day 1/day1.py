def main():
    input = []
    with open('day1_input.txt') as f:
        for line in f:
            input.append(int(line))
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

def part1(input):
    for num in input:
        if 2020-num in input:
            return num * (2020-num)

def part2(input):
    for num in input:
        goal = 2020-num
        for other_num in input:
            if goal-other_num in input:
                return num * other_num * (goal-other_num)

if __name__ == '__main__':
    main()