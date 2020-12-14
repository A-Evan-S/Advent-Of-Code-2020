import re

def main():
    input = []
    with open('day14_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

def part1(input):
    mem = dict()
    for line in input:
        if line.startswith("mask = "):
            mask = line[7:]
            print(f'mask = {mask}')
        else:
            index, val = re.match(r"mem\[(\d+)\] = (\d+)", line).groups()
            print(f'[{index}] {val} -> {apply_mask(mask, int(val))}')
            mem[int(index)] = apply_mask(mask, int(val))
    return sum(mem.values())

def apply_mask(mask, val):
    binary = bin(val)[2:].zfill(36)
    result = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += binary[i]
        elif mask[i] == '1':
            result += '1'
        else:
            result += '0'
    return int(result, 2)

def apply_mask_v2(mask, index):
    binary = bin(index)[2:].zfill(36)
    return apply_mask_v2_helper(mask, binary, '')

def apply_mask_v2_helper(mask, index, start):
    new_index = start
    result = []
    for i in range(len(mask)):
        if mask[i] == '0':
            new_index += index[i]
        elif mask[i] == '1':
            new_index += '1'
        else:
            new_index_1 = new_index + '0'
            new_index_2 = new_index + '1'
            result.extend(apply_mask_v2_helper(mask[i+1:], index[i+1:], new_index_1))
            result.extend(apply_mask_v2_helper(mask[i+1:], index[i+1:], new_index_2))
            return result
    return [int(new_index, 2)]

def part2(input):
    mem = dict()
    for line in input:
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            index, val = re.match(r"mem\[(\d+)\] = (\d+)", line).groups()
            for i in apply_mask_v2(mask, int(index)):
                mem[i] = int(val)
    return sum(mem.values())

if __name__ == '__main__':
    main()
