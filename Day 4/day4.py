import re

def main():
    input = []
    with open('day4_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

def process_passports(input):
    passports = []
    current_passport = dict()
    for line in input:
        if len(line) == 0:
            current_passport.pop("cid", None)
            passports.append(current_passport)
            current_passport = dict()
        else:
            fields = line.split()
            for field in fields:
                key, val = field.split(':')
                current_passport[key] = val
    current_passport.pop("cid", None)
    passports.append(current_passport)
    return passports

def part1(input):
    passports = process_passports(input)

    num_valid = 0
    for passport in passports:
        if len(passport) == 7:
            num_valid += 1

    return num_valid

def part2(input):
    passports = process_passports(input)

    num_valid = 0
    for passport in passports:
        if len(passport) == 7 and check_valid(passport):
            num_valid += 1

    return num_valid

def check_valid(passport):
    byr = int(passport['byr'])
    if (byr < 1920 or byr > 2002):
        print("Rejected, birth year",passport['byr'])
        return False
    iyr = int(passport['iyr'])
    if (iyr < 2010 or iyr > 2020):
        print("Rejected, issue year",passport['iyr'])
        return False
    eyr = int(passport['eyr'])
    if (eyr < 2020 or eyr > 2030):
        print("Rejected, expiration year",passport['eyr'])
        return False
    hgt = passport['hgt']
    if (hgt[-2:] == 'cm'):
        hgt = int(hgt[:-2])
        if (hgt < 150 or hgt > 193):
            print("Rejected, height cm", passport['hgt'])
            return False
    elif (hgt[-2:] == 'in'):
        hgt = int(hgt[:-2])
        if (hgt < 59 or hgt > 76):
            print("Rejected, height in", passport['hgt'])
            return False
    else:
        print("Rejected, height invalid", passport['hgt'])
        return False
    if (re.match('^#[\da-f]{6}$', passport['hcl']) == None):
        print("Rejected hair color", passport['hcl'])
        return False
    if (re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']) == None):
        print("Rejected eye color", passport['ecl'])
        return False
    if (re.match('^\d{9}$', passport['pid']) == None):
        print("Rejected passport id",passport['pid'])
        return False
    print("approved",passport)
    return True


if __name__ == '__main__':
    main()