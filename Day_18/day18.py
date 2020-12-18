from aoc_utils import timed
import re

def main():
    input = []
    with open('day18_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    result = 0
    for line in input:
        result += int(evaluate(line))
    return result

def part2(input):
    result = 0
    for line in input:
        result += int(evaluate2(line))
    return result

def evaluate(input):
    if m := re.search(r'\([^\(\)]*?\)', input):
        return evaluate(input[:m.start()] + evaluate(m.group()[1:-1]) + input[m.end():])
    elif m := re.match('^\d+ [\+\*] \d+', input):
        return evaluate(str(eval(m.group())) + input[m.end():])
    else:
        return input

def evaluate2(input):
    if m := re.search(r'\([^\(\)]*?\)', input):
        input = input[:m.start()] + evaluate2(m.group()[1:-1]) + input[m.end():]
        return evaluate2(input)
    elif m := re.search('\d+ \+ \d+', input):
        a, op, b = m.group().split()
        return evaluate2(input[:m.start()] + str(int(a) + int(b)) + input[m.end():])
    elif m := re.search('\d+ \* \d+', input):
        a, op, b = m.group().split()
        return evaluate2(input[:m.start()] + str(int(a) * int(b)) + input[m.end():])
    else:
        return input

if __name__ == '__main__':
    main()
