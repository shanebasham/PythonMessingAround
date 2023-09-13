import re

# Prints all recipes from a text file containing an ingredient the user inputs
def recipe_finder():
    try:
        # Get ingredient from user
        ingredient = input('Please enter your ingredient here: ').lower()
        # Open the recipe file
        with open('recipes.txt', 'r') as file:
            # Read the file contents into a string
            recipe = file.read()
            # Find all instances of the ingredient in the recipe
            matches = re.findall(ingredient, recipe)
            # If no matches found, print error message
            if not matches:
                print('There are no recipes containing this ingredient, please try again.')
                main()
            # Print the recipes with the ingredient highlighted
            for match in matches:
                recipe = recipe.replace(match, f'\033[1m{match}\033[0m')
                if recipe[0].isdigit():
                    print(recipe)
    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")
    return recipe

def print_recipes():
    try:
        for match in recipe_finder():
            recipe = recipe.replace(match, f'\033[1m{match}\033[0m')
            print(recipe)
    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

def main():
    recipe_finder()
    print_recipes()
    exit()

if __name__ == "__main__":
    main()

