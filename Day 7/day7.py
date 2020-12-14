import re

def main():
    input = []
    with open('day7_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

def process_rules(input):
    bag_rules = dict()
    for line in input:
        m = re.match('^(.+) bags contain( \d+ .* bags?| no other bags)\.', line)
        main_color = m.groups()[0]
        rules = re.findall(' \d+ \w+ \w+ bags?,?', m.groups()[1])
        fixed_rules = []
        for rule in rules:
            r = re.match(' (\d+) (\w+ \w+) bags?', rule).groups()
            fixed_rules.append((r[0], r[1]))
        bag_rules[main_color] = fixed_rules
    return bag_rules

def part1(input):
    bag_rules = process_rules(input)
    count = 0
    for starting_color in bag_rules:
        if can_contain_shiny(bag_rules, starting_color):
            count += 1
    return count

def can_contain_shiny(bag_rules, starting_color):
    for storable in bag_rules[starting_color]:
        if storable[1] == 'shiny gold':
            return True
    for storable in bag_rules[starting_color]:
        if can_contain_shiny(bag_rules, storable[1]):
            return True
    return False

def part2(input):
    bag_rules = process_rules(input)
    return count_required_bags(bag_rules, 'shiny gold') - 1

def count_required_bags(bag_rules, starting_bag):
    num_bags = 1
    for storable in bag_rules[starting_bag]:
        num_bags += int(storable[0]) * count_required_bags(bag_rules, storable[1])
    return num_bags
if __name__ == '__main__':
    main()