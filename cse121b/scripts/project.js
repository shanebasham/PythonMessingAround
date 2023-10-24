const fs = require('fs');

function main() {
        const filename = "recipes.txt";
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        rl.question('Please enter an ingredient: ', (ingredient) => {
            ingredientMatch(filename, ingredient);
            const openedFile = readList(filename);
            console.log(openedFile);
            const splitFile = findLinesBetweenTwoLines(filename);
            console.log(splitFile);
            printRecipesContainingIngredient(filename, ingredient);
            rl.close();
        });
}

// Prints all lines in the text file between two lines containing strings longer than 25 characters
function findLinesBetweenTwoLines(filename) {
    const recipeList = [];
    const lines = fs.readFileSync(filename, 'utf-8').split('\n');
    let startIndex = null;
    let endIndex = null;

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        if (line[0].match(/\d/) && line.length < 50) {
            startIndex = i;
        }
        if (startIndex !== null && line.length <= 50) {
            endIndex = i;
        }
        if (startIndex !== null && endIndex !== null) {
            for (let j = startIndex; j <= endIndex; j++) {
                recipeList.push(lines[j]);
            }
        }
    }

    return recipeList;
}

// Check if ingredient is in any recipes
function ingredientMatch(filename, ingredient) {
    const recipe = fs.readFileSync(filename, 'utf-8');
    const matches = recipe.match(new RegExp(ingredient, 'g'));
    if (!matches) {
        console.log(`\nThere are no recipes containing "${ingredient}" please try again!`);
        main();
    }
}

// Prints all recipes containing ingredient from user input
function printRecipesContainingIngredient(filename, ingredient) {
    const recipes = findLinesBetweenTwoLines(filename);
    for (let i = 0; i < recipes.length; i++) {
        let recipe = recipes[i].replace(ingredient, `\x1B[1m${ingredient}\x1B[0m`);
        if (recipe.includes(ingredient)) {
            console.log(recipe);
        }
    }
}

// Reads contents of a text file into a list and returns the list
function readList(filename) {
    const textList = fs.readFileSync(filename, 'utf-8').split('\n');
    return textList;
}

main();