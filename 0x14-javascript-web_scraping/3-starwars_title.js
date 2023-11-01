#!/usr/bin/node
// The script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, res, content) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(content).title);
  }
});
