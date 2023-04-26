#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, reponse, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    if (film.characters.includes(character)) {
      count++;
    }
  }
  console.log(count);
});
