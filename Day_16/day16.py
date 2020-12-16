import re
from aoc_utils import timed

def main():
    input = []
    with open('day16_input.txt') as f:
        input = f.read()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

class Rule:
    def __init__(self, rule_str):
        grps = re.match(f'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)', rule_str).groups()
        self.name = grps[0]
        self.bound_1_lower = int(grps[1])
        self.bound_1_upper = int(grps[2])
        self.bound_2_lower = int(grps[3])
        self.bound_2_upper = int(grps[4])

    def check_bound(self, val):
        return (self.bound_1_lower <= val <= self.bound_1_upper) or (self.bound_2_lower <= val <= self.bound_2_upper)

def prepare_input(input):
    rules, my_ticket, other_tickets = input.split('\n\n')
    my_ticket = my_ticket.split('\n')[1].split(',')
    for i in range(len(my_ticket)):
        my_ticket[i] = int(my_ticket[i])
    other_tickets = other_tickets.split('\n')[1:]
    for i in range(len(other_tickets)):
        vals = []
        for val in other_tickets[i].split(','):
            vals.append(int(val))
        other_tickets[i] = vals
    rules = rules.split('\n')
    for i in range(len(rules)):
        rules[i] = Rule(rules[i])
    return rules, my_ticket, other_tickets

def part1(input):
    rules, my_ticket, other_tickets = prepare_input(input)
    invalid_sum = 0
    for ticket in other_tickets:
        for val in ticket:
            valid = False
            for rule in rules:
                if rule.check_bound(val):
                    valid = True
            if not valid:
                invalid_sum += val
    return invalid_sum

def part2(input):
    rules, my_ticket, other_tickets = prepare_input(input)

    # remove invalid tickets
    valid_tickets = []
    for ticket in other_tickets:
        ticket_valid = True
        for val in ticket:
            val_valid = False
            for rule in rules:
                if rule.check_bound(val):
                    val_valid = True
            if not val_valid:
                ticket_valid = False
        if ticket_valid:
            valid_tickets.append(ticket)

    potential_matches = [[True for _ in range(len(rules))] for _ in range(len(rules))]

    for ticket in valid_tickets:
        for i in range(len(ticket)):
            for j in range(len(rules)):
                if not rules[j].check_bound(ticket[i]):
                    potential_matches[j][i] = False

    while (count2D(potential_matches) > len(potential_matches)):
        for i in range(len(potential_matches)):
            if potential_matches[i].count(True) == 1:
                known_val = potential_matches[i].index(True)
                for k in range(len(potential_matches)):
                    if i != k:
                        potential_matches[k][known_val] = False

    output = 1
    for i in range(len(potential_matches)):
        if rules[i].name.startswith('departure'):
            pos = potential_matches[i].index(True)
            output *= my_ticket[pos]
    return output

def count2D(arr):
    count = 0
    for row in arr:
        for val in row:
            if val:
                count += 1
    return count

if __name__ == '__main__':
    main()