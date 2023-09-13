import re

def main():
    try:
        filename = "recipes.txt"
        ingredient = input('Please enter an ingredient: ')
        ingredient_match(filename, ingredient)
        opened_file = read_list(filename)
        print(opened_file)
        split_file = find_lines_between_two_lines(filename)
        print(split_file)
        recipes = print_recipes_containing_ingredient(filename, ingredient)
    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")
    return recipes

#Prints all lines in the text file between two lines containing strings longer than 25 characters
def find_lines_between_two_lines(filename):
    recipe_list = []
    with open(filename, "r") as f:
        lines = f.readlines()
        start_index = 0
        end_index = 0
        for i, line in enumerate(lines):
            if line[0].isdigit() and len(line) < 50:
                start_index = i
            if start_index is not None and len(line) <= 50:
                end_index = i
            if start_index is not None and end_index is not None:
                for j in range(start_index, end_index + 1):
                    recipe_list.append(lines[j])
    return recipe_list

#Check if ingredient is in any recipes
def ingredient_match(filename, ingredient):
    with open(filename, 'r') as file:
        # Read the file contents into a string
        recipe = file.read()
        matches = re.findall(ingredient, recipe)
        # If no matches found, print error message
        if not matches:
            print(f'\nThere are no recipes containing "{ingredient}" please try again!')
            main()

#Prints all recipes containing ingredient from user input
def print_recipes_containing_ingredient(filename, ingredient):
    recipes = find_lines_between_two_lines(filename)
    for recipe in recipes:
        recipe = recipe.replace(ingredient, f'\033[1m{ingredient}\033[0m')
        if ingredient in recipe:
            print(recipe)

#Reads contents of a text file into a list and returns the list
def read_list(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list


if __name__ == "__main__":
    main()