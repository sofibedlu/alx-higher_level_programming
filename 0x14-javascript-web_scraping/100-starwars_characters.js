#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
