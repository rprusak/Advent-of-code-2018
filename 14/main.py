import sys


# part 1
def calculate_score(receipes_count: int):
    first_recipe_index = 0
    second_recipe_index = 1

    recipes = [3, 7]

    while len(recipes) < receipes_count + 10:
        new_recipe_value = recipes[first_recipe_index] + recipes[second_recipe_index]
        recipes.extend([int(x) for x in str(new_recipe_value)])
        first_recipe_index = (first_recipe_index + recipes[first_recipe_index] + 1) % len(recipes)
        second_recipe_index = (second_recipe_index + recipes[second_recipe_index] + 1) % len(recipes)

    return int("".join([str(x) for x in recipes[receipes_count:receipes_count + 10]]))


# part 2
def calculate_recipes_before(pattern: str):
    first_recipe_index = 0
    second_recipe_index = 1

    recipes = [3, 7]

    # xD
    for i in range(0, 20000000):
        new_recipe_value = recipes[first_recipe_index] + recipes[second_recipe_index]
        recipes.extend([int(x) for x in str(new_recipe_value)])
        first_recipe_index = (first_recipe_index + recipes[first_recipe_index] + 1) % len(recipes)
        second_recipe_index = (second_recipe_index + recipes[second_recipe_index] + 1) % len(recipes)

    index = "".join([str(x) for x in recipes]).find(pattern)
    if index != -1:
        return index


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py <recipes count>")
        exit()

    input_value = sys.argv[1]

    print(calculate_score(int(input_value)))
    print(calculate_recipes_before(input_value))