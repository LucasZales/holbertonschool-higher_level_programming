#!/usr/bin/node

const toggle = document.getElementById('toggle_header');
const head = document.querySelector('header');

toggle.addEventListener('click', () => {
  if (head.style.color === 'red') {
    head.style.color = '#00FF00';
  } else {
    head.style.color = 'red';
  }
});
