from collections import defaultdict
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
    recipes = parse_recipes(input)
    possible_allergens = find_possible_allergens(recipes)
    safe = list(map(lambda x: x[0], filter(lambda e: len(e[1]) == 0, possible_allergens.items())))
    return sum(recipe[0].count(safe_ingredient) for safe_ingredient in safe for recipe in recipes)

def part2(input):
    recipes = parse_recipes(input)
    possible_allergens = [[k, v] for k, v in find_possible_allergens(recipes).items()]
    possible_allergens = list(filter(lambda x: len(x[1]) > 0, possible_allergens))
    for i in range(len(possible_allergens)):
        for j in range(i + 1, len(possible_allergens)):
            possible_allergens = sorted(possible_allergens, key=lambda x: len(x[1]))
            possible_allergens[j][1] -= possible_allergens[j][1].intersection(possible_allergens[i][1])
    possible_allergens = sorted(possible_allergens, key=lambda x: list(x[1])[0])
    return ','.join(x[0] for x in possible_allergens)

def parse_recipes(input):
    recipes = []
    for line in input:
        ingredient_text, allergen_text = line.split('(contains ')
        ingredients = re.findall(r'\w+', ingredient_text)
        allergens = list(map(lambda x: x.strip(), allergen_text[:-1].split(', ')))
        recipes.append([ingredients, allergens])
    return recipes

def find_possible_allergens(recipes):
    ingredients_map = defaultdict(lambda: set())
    for recipe in recipes:
        for ingredient in recipe[0]:
            ingredients_map[ingredient].update(recipe[1])

    for recipe in recipes:
        for allergen in recipe[1]:
            for ingredient in ingredients_map.keys():
                if ingredient not in recipe[0] and (allergen in ingredients_map[ingredient]):
                    ingredients_map[ingredient].remove(allergen)

    return ingredients_map

if __name__ == '__main__':
    main()
