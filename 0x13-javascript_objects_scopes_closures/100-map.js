#!/usr/bin/node
// mapping new array from given

const array = require('./100-info.js').list;

console.log(array);
let cont = 0;
const map1 = array.map(function (x) {
  return (x * cont++);
});
console.log(map1);
