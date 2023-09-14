#!/usr/bin/node
// Script imports a dictionary of occurrences by user id

const { dict } = require('./101-data.js');
const new_dict = {};
for (const i in dict) {
    if (new_dict[dict[i]] === undefined) {
	new_dict[dict[i]] = [];
    }
    new_dict[dict[i]].push(i);
}
console.log(new_dict);
