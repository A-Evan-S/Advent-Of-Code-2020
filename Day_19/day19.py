from aoc_utils import timed
import re

def main():
    input = open('day19_input.txt').read()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    return solve(input)

def part2(input):
    return solve(input, True)

class Rule:
    def __init__(self, rule):
        if m := re.match(r'"\w"', rule):
            self.type = 'letter'
            self.letter = m.group()[1]
        else:
            self.type = 'set'
            self.rule_options = rule.split('|')
            for i in range(len(self.rule_options)):
                self.rule_options[i] = list(map(lambda x: int(x), re.findall('\d+', self.rule_options[i])))

    def check_valid(self, messages, rules):
        valid_messages = []
        for message in messages:
            if self.type == 'letter':
                if message.find(self.letter) == 0:
                    valid_messages.append(message[1:])
            else:
                for option in self.rule_options:
                    new_messages = [message]
                    option_valid = True
                    for rule in option:
                        valid, new_messages = rules[rule].check_valid(new_messages, rules)
                        if not valid:
                            option_valid = False
                            break
                    if option_valid:
                        valid_messages.extend(new_messages)
        return len(valid_messages) > 0, valid_messages

def solve_helper(message, rules):
    valid, remaining = rules[0].check_valid([message], rules)
    return valid and '' in remaining

def solve(input, part2=False):
    rule_input, messages = input.split('\n\n')
    rules = {}
    for rule in rule_input.split('\n'):
        rule_num, rule_text = rule.split(': ')
        rules[int(rule_num)] = Rule(rule_text)

    if part2:
        max_rec = 6
        rules[8] = Rule('|'.join(['42 '*i for i in range(1, max_rec)]))
        rules[11] = Rule('|'.join(['42 '*i + '31 '*i for i in range(1, max_rec)]))

    return len(list(filter(lambda m: solve_helper(m, rules), messages.split('\n'))))

if __name__ == '__main__':
    main()
