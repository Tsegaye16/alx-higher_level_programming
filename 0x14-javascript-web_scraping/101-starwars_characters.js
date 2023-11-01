#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, res, content) {
  if (!err) {
    const characters = JSON.parse(content).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (err, res, content) {
    if (!err) {
      console.log(JSON.parse(content).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
