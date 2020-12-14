def main():
    input = []
    length = 25
    with open('day9_input.txt') as f:
        for line in f:
            input.append(int(line.strip()))
    print("Part 1:", part1(input, length))
    print("Part 2:", part2(input, length))

def part1(input, length):
    for i in range(length,len(input)):
        prev_values = input[i-length:i]
        val = input[i]
        found = False
        for a in prev_values:
            if (val - a) in prev_values:
                found = True
        if not found:
            return val
    raise RuntimeError("No Invalid Value Found")

def part2(input, length):
    goal = part1(input, length)
    i, j = part2helper(goal, input)
    return min(input[i:j+1]) + max(input[i:j+1])

def part2helper(goal, input):
    for i in range(len(input)):
        sum = input[i]
        for j in range(i+1, len(input)):
            sum += input[j]
            if sum == goal:
                return i, j
            elif sum > goal:
                break
    raise RuntimeError("No Appropriate Sequence Found")

if __name__ == '__main__':
    main()