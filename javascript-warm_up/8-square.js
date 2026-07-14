#!/usr/bin/node

const args = process.argv.slice(2);
const veces = parseInt(args[0]);

if (isNaN(veces)) {
  console.log('Missing size');
} else {
  for (let fila = 0; fila < veces; fila++) {
    console.log('X'.repeat(veces));
  }
}
