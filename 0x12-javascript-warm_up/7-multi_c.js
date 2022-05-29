#!/usr/bin/node
if (isNaN(process.argv[2])){
  console.log('Missing number of occurrences');
}
const myVar = ('C is fun');
for (let i = 0; i < process.argv[2]; i++) {
  console.log(myVar);
}

