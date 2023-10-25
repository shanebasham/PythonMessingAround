// Declare and initialize global variables
const recipesElement = document.querySelector('#recipes');
let recipeList = [];

// async displayRecipes Function
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

// async getRecipes Function using fetch()
const getRecipes = async () => {
    const response = await fetch("https://shanebasham.github.io/PythonMessingAround/cse121b/scripts/recipes.json");
    recipeList = await response.json();
    displayRecipes(recipeList);
};

// get the finder div element so we can do something with it
const finderElement = document.getElementById('finder');
// get the form so we can read what was entered in it
const formElement = document.forms[0];
// add listener to wait for a submission of form to run the code
formElement.addEventListener('submit', function(e) {
    // stop form from doing the default action.
    e.preventDefault();
    // set the contents of finder element to a message letting the user know the form was submitted successfully. Notice that we pull the name that was entered in the form to personalize the message!
    getRecipes();
});

// reset Function
const reset = () => {
    recipesElement.innerHTML = '';
};

// // if recipeList contains user input ingredient append to innerhtml
// const searchRecipes = (recipes) => {
//     reset();
//     var ingredient = document.getElementById('ingredient').value;
//     let article = document.createElement('article');
//     switch (document.querySelector('#ingredient').value) {
//         case (recipeList.includes(ingredient)):
//             displayRecipes(recipes);
//             break;
//         default:
//             printError()
//     };
// };

// function printError(ingredient) {
//     document.getElementById('printError').innerHTML = ingredient;
//     console.log(ingredient); 
// };