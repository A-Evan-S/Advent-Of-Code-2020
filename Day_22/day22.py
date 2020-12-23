import copy
from aoc_utils import timed


def main():
    with open('day22_input.txt') as f:
        input = f.read()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))


def part1(input):
    p1_hand, p2_hand = parse_input(input)

    while len(p1_hand) > 0 and len(p2_hand) > 0:
        card1 = p1_hand.pop(0)
        card2 = p2_hand.pop(0)
        if card1 > card2:
            p1_hand.extend([card1, card2])
        else:
            p2_hand.extend([card2, card1])

    return max(score(p1_hand), score(p2_hand))


def part2(input):
    p1_hand, p2_hand = parse_input(input)
    play_recursive(p1_hand, p2_hand)
    return max(score(p1_hand), score(p2_hand))


def parse_input(input):
    p1_input, p2_input = input.split('\n\n')
    p1_hand = [int(n) for n in p1_input.split('\n')[1:]]
    p2_hand = [int(n) for n in p2_input.split('\n')[1:]]
    return p1_hand, p2_hand


def score(hand):
    return sum(hand[i] * (len(hand) - i) for i in range(len(hand)))


def play_recursive(p1_hand, p2_hand, top_level=True):
    # Skip easily provable win scenarios
    if not top_level and 50 in p1_hand:
        return 1
    elif not top_level and 50 in p2_hand:
        return 2

    prev_hands = set()
    while len(p1_hand) > 0 and len(p2_hand) > 0:
        if str(p1_hand) + '|' + str(p2_hand) in prev_hands:
            return 1
        prev_hands.add(str(p1_hand) + '|' + str(p2_hand))

        card1 = p1_hand.pop(0)
        card2 = p2_hand.pop(0)

        if len(p1_hand) >= card1 and len(p2_hand) >= card2:
            p1_hand_copy = copy.deepcopy(p1_hand[:card1])
            p2_hand_copy = copy.deepcopy(p2_hand[:card2])
            winner = play_recursive(p1_hand_copy, p2_hand_copy, False)
            if winner == 1:
                p1_hand.extend([card1, card2])
            else:  # winner == 2
                p2_hand.extend([card2, card1])
        else:
            if card1 > card2:
                p1_hand.extend([card1, card2])
            else:
                p2_hand.extend([card2, card1])
    return 1 if len(p2_hand) == 0 else 2


if __name__ == '__main__':
    main()
