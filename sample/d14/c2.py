class Recipe:
    def __init__(self, score, next):
        self.score = score
        self.next = next


def main():
    needed_recipes = 0
    for line in open("input.txt"):
        needed_recipes = int(line)

    start_recipe = Recipe(3, None)
    last_recipe = Recipe(7, start_recipe)
    start_recipe.next = last_recipe
    recipe_1elf = start_recipe
    recipe_2elf = last_recipe
    size = 2
    steps = 20216200
    for _ in range(steps):
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

    current_recipe = start_recipe
    array_input = [int(i) for i in str(needed_recipes)]
    validation = 0
    current_recipe_id = 1
    start_test = current_recipe
    while True:
        if current_recipe.score == array_input[validation]:
            if validation == 0:
                start_test = current_recipe
                start_test_recipe_id = current_recipe_id
            validation += 1
            if validation == len(array_input):
                print(current_recipe_id - len(array_input))
                exit(1)
            current_recipe = current_recipe.next
            current_recipe_id += 1
        else:
            if validation > 0:
                validation = 0
                current_recipe = start_test.next
                current_recipe_id = start_test_recipe_id + 1
            else:
                current_recipe = current_recipe.next
                current_recipe_id += 1
        if current_recipe == start_recipe:
            exit(2)


if __name__ == '__main__':
    main()

