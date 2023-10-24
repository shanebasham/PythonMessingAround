
/* Declare and initialize global variables */
const recipesElement = document.querySelector('#recipes');
let recipeList = [];

/* async displayRecipes Function */
const displayRecipes = (recipes) => {
    recipes.forEach((recipe) => { 
        let article = document.createElement('article');
        let recipeName = document.createElement('h2');
        let ingredients = document.createElement('h3');
        let instructions = document.createElement('h3');
        recipeName.textContent = recipe.recipeName;
        ingredients.textContent = recipe.ingredients;
        instructions.textContent = recipe.instructions;
        article.appendChild(recipeName);
        article.appendChild(ingredients);
        article.appendChild(instructions);
        recipesElement.appendChild(article)});
};

/* async getRecipes Function using fetch()*/
const getRecipes = async () => {
    const response = await fetch("https://shanebasham.github.io/PythonMessingAround/cse121b/scripts/recipes.json");
    recipeList = await response.json();
    displayRecipes(recipeList);
};

// /* reset Function */
// const reset = () => {
//     recipesElement.innerHTML = '';
// };

// /* sortBy Function */
// const sortBy = (recipes) => {
//     reset();
//     switch (document.querySelector('#sortBy').value) {
//         case 'utah':
//             displayRecipes(recipes.filter(temple => temple.location.includes('Utah')));
//             break;
//         case 'notutah':
//             displayRecipes(recipes.filter(temple => !temple.location.includes('Utah')));
//             break;
//         case 'older':
//             displayRecipes(recipes.filter(temple => new Date(temple.dedicatedDate) < new Date(1950, 0, 1)));
//             break;
//         case 'all':
//             displayRecipes(recipes);
//             break;
//     };
// }

getRecipes();


// /* Event Listener */
// document.querySelector('#sortBy').addEventListener('change', () => { sortBy(recipeList) });