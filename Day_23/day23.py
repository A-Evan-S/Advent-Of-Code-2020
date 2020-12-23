from aoc_utils import timed


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def main():
    with open('day23_input.txt') as f:
        input = f.readline()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))


def get_range(list, start, end):
    if end < len(list):
        return list[start:end]
    elif start < len(list):
        return list[start:] + list[:end % len(list)]
    else:
        return list[start % len(list):end % len(list)]


def part1(input):
    cups = [int(c) for c in input]

    curr_cup_index = 0
    for i in range(100):
        next_label = cups[(curr_cup_index + 4) % len(cups)]
        curr_cup_label = cups[curr_cup_index]
        three_temp = get_range(cups, curr_cup_index + 1, curr_cup_index + 4)
        cups = [x for x in cups if x not in three_temp]
        destination_cup_label = curr_cup_label - 1
        while destination_cup_label not in cups:
            destination_cup_label -= 1
            if destination_cup_label < 1:
                destination_cup_label = 9
        destination_cup_index = cups.index(destination_cup_label)
        cups = cups[:destination_cup_index + 1] + three_temp + cups[destination_cup_index + 1:]
        curr_cup_index = cups.index(next_label)

    one_index = cups.index(1)
    result = ''
    for i in range(one_index + 1, one_index + len(cups)):
        result += str(cups[i % len(cups)])
    return result


def display(curr_node):
    print(f'({curr_node.val}) ', end='')
    temp = curr_node.next
    while temp != curr_node:
        print(f'{temp.val} ', end='')
        temp = temp.next
    print()


def part2(input):
    cups = [int(c) for c in input] + list(range(10, 1000001))
    node_locations = {}

    last_node = Node(cups.pop(-1), None)
    node_locations[last_node.val] = last_node
    curr_node = last_node
    while len(cups) > 0:
        curr_node = Node(cups.pop(-1), curr_node)
        node_locations[curr_node.val] = curr_node
    last_node.next = curr_node
    for i in range(10000000):
        three_temp = curr_node.next
        excluded_vals = curr_node.val, three_temp.val, three_temp.next.val, three_temp.next.next.val
        curr_node.next = curr_node.next.next.next.next
        dest = curr_node.val
        while dest in excluded_vals:
            dest -= 1
            if dest < 1:
                dest = 1000000
        temp_node = node_locations[dest]
        after = temp_node.next
        temp_node.next = three_temp
        three_temp.next.next.next = after
        curr_node = curr_node.next
    curr_node = node_locations[1]
    val_1 = curr_node.next.val
    val_2 = curr_node.next.next.val
    return val_1 * val_2

if __name__ == '__main__':
    main()