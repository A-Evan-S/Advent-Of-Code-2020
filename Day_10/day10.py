from aoc_utils import timed


def main():
    input = []
    with open('day10_input.txt') as f:
        for line in f:
            input.append(int(line.strip()))
    input.sort()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    gaps = [0, 0, 0, 1]
    gaps[input[0]] += 1
    for i in range(1, len(input)):
        gaps[input[i] - input[i-1]] += 1
    return gaps[1] * gaps[3]

def part2(input):
    arr = [1] + [0 for i in range(max(input)-1)]
    for i in range(len(arr)):
        if i in input:
            arr[i] = sum(arr[max(0, i-3):i])
    return sum(arr[-3:])

if __name__ == '__main__':
    main()
