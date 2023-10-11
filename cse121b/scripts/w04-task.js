/* LESSON 3 - Programming Tasks */

/* Profile Object  */

let myProfile = {
    name: 'Shane Basham',
    photo: 'images/me.jpg',
    favoriteFoods : ['Cherries', 'Cherry Pie', 'Cherry Cheese Cake', 'Cherry Ice Cream'],
    hobbies: ['Art', 'Running', 'Learning Languages', 'Wood Turning'],
    placesLived: []
  };


/* Populate Profile Object with placesLive objects */

myProfile.placesLived.push(
    {
      place: 'Tucson Arizona',
      length: '20 years'
    },
    {
      place: 'Springville Utah',
      length: '1 year'
    }
  );

/* DOM Manipulation - Output */

/* Name */
document.querySelector('#name').textContent = myProfile.name;

/* Photo with attributes */
document.getElementById('#photo').src = photo;
document.getElementById('#photo').alt = name;

/* Favorite Foods List*/
myProfile.favoriteFoods.forEach(food => {
    let li = document.createElement('li');
    li.textContent = food;
    document.querySelector('#favorite-foods').appendChild(li);
  });

/* Hobbies List */
myProfile.hobbies.forEach(hobby => {
    let li = document.createElement('li');
    li.textContent = hobby;
    document.querySelector('#hobbies').appendChild(li);
  });

/* Places Lived DataList */
myProfile.placesLived.forEach(place => {
    let dt = document.createElement('dt');
    dt.textContent = place;
    document.querySelector('#place').appendChild(dt);
  });
myProfile.placesLived.forEach(length => {
    let dd = document.createElement('dd');
    dd.textContent = length;
    document.querySelector('#length').appendChild(dd);
  });

