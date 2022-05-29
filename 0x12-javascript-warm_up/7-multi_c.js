#!/usr/bin/node

#print c is fun as many as argv[2]
const myVar = 'C is fun';
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    console.log(myVar);
  }
}
