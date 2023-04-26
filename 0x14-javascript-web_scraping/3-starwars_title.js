#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const path = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(path, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body).title;
  console.log(data);
});
