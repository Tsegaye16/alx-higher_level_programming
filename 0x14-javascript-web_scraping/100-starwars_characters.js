#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (err, res, content) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(content);
  const dd = data.characters;
  for (const i of dd) {
    req.get(i, function (err, res, content1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(content1);
      console.log(data1.name);
    });
  }
});
