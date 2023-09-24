/* W02-Task - Profile Home Page */

/* Step 1 - Setup type tasks - no code required */

/* Step 2 - Variables */

let fullName = 'Shane Basham';
let currentYear = '2023';
let profilePicture = 'images/me.jpg';

/* Step 3 - Element Variables */

const nameElement = document.getElementById('name');
const foodElement = document.getElementById('food');
const yearElement = document.getElementById('#year');
const imageElement = document.getElementById('image');

/* Step 4 - Adding Content */

nameElement.innerHTML = '<strong>Shane Basham</strong>';
let text = currentYear.textContent;
imageElement.setAttribute('src', profilePicture);
imageElement.setAttribute('alt', `Profile image of ${fullName}`);

/* Step 5 - Array */

let food = ['Cherries', 'Cherry Pie', 'Cherry Cheese Cake', 'Cherry Ice Cream'];
foodElement.innerHTML = food;
food.push('Cherry Bread');
foodElement.innerHTML += `<br>${food}`;
food.shift();
foodElement.innerHTML += `<br>${food}`;
food.pop();
foodElement.innerHTML += `<br>${food}`;


