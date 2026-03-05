from collections import defaultdict


foods = []
all_ingreds = []
with open('input/input21.txt') as f:
    for line in f:
        line = line.strip()
        line = line[:-1]

        ingredients, allergens = line.split(' (contains ')
        allergens = allergens.split(', ')

        ingredients = ingredients.split(' ')

        foods.append((allergens, ingredients))
        all_ingreds += ingredients
all_ingreds = set(all_ingreds)

# Dictionary contains list of list of ingredients for each food that contains an allergen.
allergen_foods = defaultdict(list)
for f in foods:
    a_list, i = f
    for a in a_list:
        allergen_foods[a].append(i)

maybe_bad_ingredients = []
allergen_ingreds = dict()
for a, ingred_list in allergen_foods.items():
    maybe_bad = set(ingred_list[0])
    for i in range(1, len(ingred_list)):
        maybe_bad &= set(ingred_list[i])

    maybe_bad_ingredients += list(maybe_bad)
    allergen_ingreds[a] = maybe_bad
maybe_bad_ingredients = set(maybe_bad_ingredients)

def_good = all_ingreds - maybe_bad_ingredients

count = 0
for f in foods:
    a_list, i = f
    for ing in i:
        if ing in def_good:
            count += 1
print(count)


def_bad = []
vals = len(sum([list(x) for x in allergen_ingreds.values()], []))
while vals > 0:
    for a, i in allergen_ingreds.items():
        if len(i) == 1:
            found = list(i)[0]
            def_bad.append((a, found))
            for b, j in allergen_ingreds.items():
                if found in j:
                    j.remove(found)
    vals = len(sum([list(x) for x in allergen_ingreds.values()], []))

def_bad = sorted(def_bad)

allergens, ingredients = zip(*def_bad)

canonical_dangerous_ingredient_list = ''
for i in ingredients:
    canonical_dangerous_ingredient_list += i
    canonical_dangerous_ingredient_list += ','
canonical_dangerous_ingredient_list = canonical_dangerous_ingredient_list[:-1]
print(canonical_dangerous_ingredient_list)
