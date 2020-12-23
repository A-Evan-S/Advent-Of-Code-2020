from aoc_utils import timed

def main():
    with open('day23_input.txt') as f:
        input = f.readline()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def part1(input):
    cups = [int(c) for c in input]
    one_node = play_game(cups, 100)
    curr_node = one_node.next
    output = ''
    while curr_node != one_node:
        output += str(curr_node.val)
        curr_node = curr_node.next
    return output


def part2(input):
    cups = [int(c) for c in input] + list(range(10, 1000001))
    one_node = play_game(cups, 10000000)
    val_1 = one_node.next.val
    val_2 = one_node.next.next.val
    return val_1 * val_2


def play_game(cups, iterations):
    node_locations = {}

    last_node = Node(cups.pop(-1), None)
    node_locations[last_node.val] = last_node
    curr_node = last_node
    while len(cups) > 0:
        curr_node = Node(cups.pop(-1), curr_node)
        node_locations[curr_node.val] = curr_node
    last_node.next = curr_node
    for i in range(iterations):
        three_temp = curr_node.next
        excluded_vals = curr_node.val, three_temp.val, three_temp.next.val, three_temp.next.next.val
        curr_node.next = curr_node.next.next.next.next
        dest = curr_node.val
        while dest in excluded_vals:
            dest -= 1
            if dest < 1:
                dest = len(node_locations)
        temp_node = node_locations[dest]
        after = temp_node.next
        temp_node.next = three_temp
        three_temp.next.next.next = after
        curr_node = curr_node.next
    return node_locations[1]

if __name__ == '__main__':
    main()
