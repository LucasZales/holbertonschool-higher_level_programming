#!/usr/bin/node

const pedir = process.argv.slice(2);
const rep = parseInt(pedir[0]);

if (pedir[0] === undefined) {
  console.log('Missing number of accurrences');
} else if (!isNaN(rep)) {
  for (let i = 0; i < rep; i++) {
    console.log('C is fun');
  }
}
