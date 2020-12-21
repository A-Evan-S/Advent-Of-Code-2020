from aoc_utils import timed
import re

def main():
    input = []
    with open('day21_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    safe = find_safe(input)
    count = 0
    for line in input:
        ing, al = line.split('(')
        ing = re.findall('\w+', ing)
        for ingredient in ing:
            if ingredient in safe:
                count += 1

    return count

def find_safe(input):
    ingredients = set()
    allergens = set()
    for line in input:
        ing, al = line.split('(')
        ingredients.update(re.findall('\w+', ing))
        allergens.update(list(map(lambda x: x.strip(), al[8:-1].split(', '))))

    ingredients_map = {}
    for ingredient in ingredients:
        ingredients_map[ingredient] = list(allergens)

    for line in input:
        ing, al = line.split('(')
        ing = re.findall('\w+', ing)
        al = list(map(lambda x: x.strip(), al[8:-1].split(', ')))
        for allergen in al:
            for ingredient in ingredients_map.keys():
                if ingredient not in ing and (allergen in ingredients_map[ingredient]):
                    ingredients_map[ingredient].remove(allergen)

    safe = []

    for ingredient in ingredients_map.keys():
        if ingredients_map[ingredient] == []:
            safe.append(ingredient)
    return safe

def part2(input):
    safe = find_safe(input)
    lines = []
    ingredients = set()
    allergens = set()
    for line in input:
        ing, al = line.split('(')
        ing = re.findall('\w+', ing)
        al = list(map(lambda x: x.strip(), al[8:-1].split(', ')))
        lines.append([ing, al])
        ingredients.update(ing)
        allergens.update(al)

    ingredients = list(filter(lambda x: x not in safe, ingredients))
    allergens = list(allergens)

    #remove known safe ingredients
    for line in lines:
        line[0] = list(filter(lambda x: x not in safe, line[0]))

    arr = [[True for _ in range(len(ingredients))] for _ in range(len(allergens))]

    for line in lines:
        for allergen in line[1]:
            for i in range(len(ingredients)):
                if ingredients[i] not in line[0]:
                    arr[allergens.index(allergen)][i] = False


    old_count = sum([row.count(True) for row in arr])
    new_count = 0

    while old_count != new_count:
        old_count = new_count
        for i in range(len(arr)):
            if arr[i].count(True) == 1:
                col_to_clear = arr[i].index(True)
                for j in range(len(arr)):
                    if i != j:
                        arr[j][col_to_clear] = False
        new_count = sum([row.count(True) for row in arr])

    for i in range(len(ingredients)):
        allergen = None
        for j in range(len(arr)):
            if arr[j][i]:
                allergen = allergens[j]
        ingredients[i] = (ingredients[i], allergen)

    ingredients = sorted(ingredients, key=lambda ing: ing[1])

    answer = ','.join(ing[0] for ing in ingredients)
    return answer

if __name__ == '__main__':
    main()