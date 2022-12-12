#!/usr/bin/node

const x = process.argv[2];

function factorial (x) {
  let aux = 1;
  if (isNaN(x) || (x === 0)) {
    return (1);
  } else {
    for (let i = 1; i <= parseInt(x); i++) {
      aux = aux * i;
    }
  }
  return (aux);
}
console.log(factorial(x));
