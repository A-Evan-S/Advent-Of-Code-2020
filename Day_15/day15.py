from aoc_utils import timed

def main():
    input = []
    with open('day15_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def find_nth_number_alt(input, n):
    nums = input[0].split(',')
    prev_nums = dict()
    curr_time = 0
    for num in nums:
        prev_nums[int(num)] = curr_time
        curr_time += 1
    next_number = 0
    while True:
        if next_number not in prev_nums.keys():
            prev_nums[next_number] = curr_time
            next_number = 0
        else:
            old_time = prev_nums[next_number]
            prev_nums[next_number] = curr_time
            next_number = curr_time - old_time
        curr_time += 1
        if curr_time == n - 1:
            return next_number

def find_nth_number(input, n):
    nums = input[0].split(',')
    prev_nums = [0] * n
    curr_time = 1
    for num in nums:
        prev_nums[int(num)] = curr_time
        curr_time += 1
    next_number = 0
    while curr_time < n:
        if not prev_nums[next_number]:
            prev_nums[next_number] = curr_time
            next_number = 0
        else:
            old_time = prev_nums[next_number]
            prev_nums[next_number] = curr_time
            next_number = curr_time - old_time
        curr_time += 1
    return next_number

def part1(input):
    return find_nth_number(input, 2020)

def part2(input):
    return find_nth_number(input, 30000000)

if __name__ == '__main__':
    main()