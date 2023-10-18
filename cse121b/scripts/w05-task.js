/* W05: Programming Tasks */

/* Declare and initialize global variables */
const templesElement = document.getElementById('temples');
let templeList = [];

/* async displayTemples Function */
const displayTemples = (temples) => {
    temples.forEach((temple) => {article = document.createElement("article"),
    header = document.createElement("h3"),
    header.innerHTML = temple.templeName,
    img = document.createElement("img"),
    img.src = temple.imageUrl,
    img.alt = temple.location,
    article.appendChild(header),
    article.appendChild(img),
    templesElement.appendChild(article)})
};

/* async getTemples Function using fetch()*/
const getTemples = async () => {
    const response = await fetch("https://byui-cse.github.io/cse121b-ww-course/resources/temples.json");
    let responseJSON = Object.assign({}, response)
    templeList.push(responseJSON)
    displayTemples(templeList)
};

/* reset Function */
const reset = function () {
    const templatesElement = document.querySelector('templates');
    const articleElements = templatesElement.querySelectorAll('article');
    articleElements.forEach(article => {
        article.remove();
    });
};

/* sortBy Function */
function sortBy(temples) {
    reset();
    let filter = document.getElementById('sortBy').value;
    switch (filter) {
        case 'utah':
            displayTemples(temples.filter(temple => temple.location.includes('Utah')));
            break;
        case 'notutah':
            displayTemples(temples.filter(temple => !temple.location.includes('Utah')));
            break;
        case 'older':
            displayTemples(temples.filter(temple => new Date(temple.dedicatedDate) < new Date(1950, 0, 1)));
            break;
        case 'all':
        default:
            displayTemples(temples);
            break;
    }
}


displayTemples();
getTemples();

/* Event Listener */

