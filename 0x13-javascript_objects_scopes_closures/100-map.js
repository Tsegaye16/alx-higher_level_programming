#!/usr/bin/node
// mapping new array from given

const array = [1, 2, 3, 4, 5];

console.log(array);
let cont = 0;
const map1 = array.map(function (x) {
  return (x * cont++);
});
console.log(map1);
