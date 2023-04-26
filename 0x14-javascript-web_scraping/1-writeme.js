#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];
const data = process.argv[3];

fs.writeFile(path, data, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
