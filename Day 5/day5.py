import re

def main():
    input = []
    with open('day5_input.txt') as f:
        for line in f:
            input.append(line)
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

def part1(input):
    sids = map(lambda x : int(re.sub('[BR]','1',re.sub('[FL]','0',x)),2), input)
    return max(sids)

def part2(input):
    sids = list(map(lambda x : int(re.sub('[BR]','1',re.sub('[FL]','0',x)),2), input))
    for i in range(min(sids), max(sids)):
        if i not in sids:
            return i
    return -1

if __name__ == '__main__':
    main()