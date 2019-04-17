class Recipe:
    def __init__(self, score, next):
        self.score = score
        self.next = next


def main():
    needed_recipes = 0
    for line in open("input.txt"):
        needed_recipes = int(line)
    extra_recipe_needed = 10
    wanted_recipes = needed_recipes + extra_recipe_needed

    start_recipe = Recipe(3, None)
    last_recipe = Recipe(7, start_recipe)
    start_recipe.next = last_recipe

    recipe_1elf = start_recipe
    recipe_2elf = last_recipe
    size = 2
    while True:
        new_score = recipe_1elf.score + recipe_2elf.score
        if new_score >= 10:
            new_last = Recipe(new_score - 10, start_recipe)
            before_last = Recipe(1, new_last)
            last_recipe.next = before_last
            last_recipe = new_last
            size += 2
        else:
            new_last = Recipe(new_score, start_recipe)
            last_recipe.next = new_last
            last_recipe = new_last
            size += 1
        for _ in range(recipe_1elf.score + 1):
            recipe_1elf = recipe_1elf.next
        for _ in range(recipe_2elf.score + 1):
            recipe_2elf = recipe_2elf.next
        if size >= wanted_recipes:
            break

    current_recipe = start_recipe
    current_recipe_id = 1
    while True:
        if needed_recipes < current_recipe_id <= wanted_recipes:
            print(current_recipe.score, end="")
        if current_recipe.next == start_recipe:
            exit(1)
        current_recipe = current_recipe.next
        current_recipe_id += 1


if __name__ == '__main__':
    main()

