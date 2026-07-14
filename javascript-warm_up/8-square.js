#!/usr/bin/node

const args = process.argv.slice(2);
const veces = parseInt(args[0]);

if (args[0] === undefined) {
  console.log('Missing size');
} else if (!isNaN(veces)) {
  for (let fila = 0; fila < veces; fila++) {
    console.log('X'.repeat(veces));
  }
}
