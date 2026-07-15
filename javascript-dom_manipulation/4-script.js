#!/usr/bin/node

const clicking = document.getElementById('add_item');
const adding = document.querySelector('.my_list');

clicking.addEventListener('click', () => {
  const new_list = document.createElement('li');
  new_list.textContent = "Item";
  adding.appendChild(new_list);
});