#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, content) {
  if (!err) {
    const results = JSON.parse(content).results;
    console.log(results.reduce((counter, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? counter + 1
        : counter;
    }, 0));
  }
});
