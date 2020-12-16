from aoc_utils import timed

def main():
    input = []
    with open('test_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    min_time = int(input[0])
    busses = []
    for bus in input[1].split(','):
        if bus != 'x':
            busses.append(int(bus))
    min_bus = busses[0]
    wait_time = min_time * 2
    for bus in busses:
        wait = (min_time // bus + 1) * bus
        if wait < wait_time:
            wait_time = wait
            min_bus = bus
    return min_bus * (wait_time - min_time)

def part2(input):
    busses = []
    i = 0
    for bus in input[1].split(','):
        if bus != 'x':
            busses.append([int(bus),i])
        i += 1
    for bus in busses:
        while bus[1] > bus[0]:
            bus[1] -= bus[0]
    steps = 0
    while len(busses) > 1:
        a = busses.pop(0)
        b = busses.pop(0)
        curr_val = a[1]
        while curr_val % b[0] != b[1]:
            steps += 1
            curr_val += a[0]
        busses.insert(0,[a[0]*b[0],curr_val])
    return busses[0][0]-busses[0][1]

if __name__ == '__main__':
    main()