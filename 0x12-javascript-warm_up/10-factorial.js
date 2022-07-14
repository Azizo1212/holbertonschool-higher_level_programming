#!/usr/bin/node

const y = process.argv[2];
function factorial (y) {
  let res = 1;
  if (isNaN(y) || (y === 0)) {
    return (1);
  } else {
    for (let i = 1; i <= parseInt(y); i++) {
      res = res * i;
    }
  }
  return (res);
}
console.log(factorial(y));
