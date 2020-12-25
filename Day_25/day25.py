from aoc_utils import timed

def main():
    input = []
    with open('day25_input.txt') as f:
        for line in f:
            input.append(int(line.strip()))
    print("Part 1:", timed(part1, input))


def part1(input):
    card_public_key, door_public_key = input
    subject_number = 7
    curr_val = 1
    card_loop_size = 0
    while curr_val != card_public_key:
        card_loop_size += 1
        curr_val *= subject_number
        curr_val %= 20201227
    return pow(door_public_key, card_loop_size, 20201227)

if __name__ == '__main__':
    main()