#!/usr/bin/node
const list = require('./100-info.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
