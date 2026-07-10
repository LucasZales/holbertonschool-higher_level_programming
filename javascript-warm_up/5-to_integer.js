#!/usr/bin/node

const args = process.argv.slice(2);
const Number = parseInt(args[0], 10);
if (Number) {
  console.log('My number:', Number);
} else {
  console.log('Not a number');
}
