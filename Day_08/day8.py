import copy
from aoc_utils import timed

def main():
    input = []
    with open('day8_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def prepare_commands(input):
    commands = []
    for command in input:
        com, val = command.split()
        val = int(val)
        commands.append([com, val, False])
    return commands

def part1(input):
    commands = prepare_commands(input)
    pos = 0
    acc = 0
    while True:
        command = commands[pos]
        if command[2]:
            return acc
        if command[0] == 'acc':
            acc += command[1]
            pos += 1
        elif command[0] == 'nop':
            pos += 1
        elif command[0] == 'jmp':
            pos += command[1]
        command[2] = True
    return 'error'

def part2(input):
    original_commands = prepare_commands(input)

    for i in range(len(original_commands)):
        test_commands = copy.deepcopy(original_commands)
        if test_commands[i][0] == 'jmp':
            test_commands[i][0] = 'nop'
        elif test_commands[i][0] == 'nop':
            test_commands[i][0] = 'jmp'
        else:
            continue
        try:
            return run_code(test_commands)
        except RecursionError:
            pass

def run_code(commands):
    pos = 0
    acc = 0
    while pos < len(commands):
        command = commands[pos]
        if command[2]:
            raise RecursionError()
        if command[0] == 'acc':
            acc += command[1]
            pos += 1
        elif command[0] == 'nop':
            pos += 1
        elif command[0] == 'jmp':
            pos += command[1]
        command[2] = True
    return acc

if __name__ == '__main__':
    main()