#!/usr/bin/node

const square = 'X';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    console.log(square.repeat(process.argv[2]));
  }
}
