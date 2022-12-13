#!/usr/bin/node

const y = require('./100-data').list;
console.log(y);

let i = 0;
const map1 = y.map(x => x * i++);
console.log(map1);
