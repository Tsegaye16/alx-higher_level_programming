#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const first_file = fs.readFileSync('./' + args[0]);
const second_file = fs.readFileSync('./' + args[1]);
fs.writeFileSync('./' + args[2], first_file + second_file);
