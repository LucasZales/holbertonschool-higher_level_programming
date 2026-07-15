#!/usr/bin/node

const clicking = document.getElementById('update_header');
const update = document.querySelector('header');

clicking.addEventListener('click', () => {
  update.textContent = 'New Header!!!';
});