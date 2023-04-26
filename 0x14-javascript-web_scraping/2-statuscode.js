#!/usr/bin/node

const request = require('request');

const path = process.argv[2];

request.get(path, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
