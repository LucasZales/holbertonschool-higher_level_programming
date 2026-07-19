#!/usr/bin/node

const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
const update = document.getElementById('character');

fetch(url)
    .then(response => response.json())
    .then(data => {
    update.textContent = data.name;
    })
    .catch(error => {
    console.error(error);
    });
