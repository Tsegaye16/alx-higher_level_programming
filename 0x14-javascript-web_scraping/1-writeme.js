#!/usr/bin/node
import fs from 'fs';
fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) console.log(err);
});
