from aoc_utils import timed
import re, copy

def main():
    input = []
    with open('day21_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))


def part1(input):
    recipes, ingredients, allergens = parse_recipes(input)
    possible_allergens = find_possible_allergens(recipes, ingredients, allergens)
    safe = list(map(lambda x: x[0], filter(lambda e: e[1] == [], possible_allergens.items())))
    return sum(recipe[0].count(safe_ingredient) for safe_ingredient in safe for recipe in recipes)


def parse_recipes(input):
    recipes = []
    all_ingredients = set()
    all_allergens = set()
    for line in input:
        ingredient_text, allergen_text = line.split('(contains ')
        ingredients = re.findall('\w+', ingredient_text)
        allergens = list(map(lambda x: x.strip(), allergen_text[:-1].split(', ')))
        recipes.append([ingredients, allergens])
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)
    return recipes, list(all_ingredients), list(all_allergens)


def find_possible_allergens(recipes, ingredients, allergens):
    ingredients_map = {}
    for ingredient in ingredients:
        ingredients_map[ingredient] = copy.deepcopy(allergens)

    for recipe in recipes:
        for allergen in recipe[1]:
            for ingredient in ingredients_map.keys():
                if ingredient not in recipe[0] and (allergen in ingredients_map[ingredient]):
                    ingredients_map[ingredient].remove(allergen)

    return ingredients_map


def part2(input):
    recipes, ingredients, allergens = parse_recipes(input)
    possible_allergens = find_possible_allergens(recipes, ingredients, allergens)
    possible_allergens = dict(filter(lambda e: len(e[1]) > 0, possible_allergens.items()))
    ingredients = list(possible_allergens.keys())

    arr = [[False for _ in range(len(ingredients))] for _ in range(len(allergens))]

    for ing, als in possible_allergens.items():
        for al in als:
            arr[allergens.index(al)][ingredients.index(ing)] = True

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

    return ','.join(ing[0] for ing in ingredients)

if __name__ == '__main__':
    main()