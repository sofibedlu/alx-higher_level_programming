#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, reponse, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const url of film.characters) {
      if (url.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
