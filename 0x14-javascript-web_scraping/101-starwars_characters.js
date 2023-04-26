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
  const promises = characters.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
  });

  Promise.all(promises)
    .then(responses => {
      for (const data of responses) {
        console.log(data.name);
      }
    })
    .catch(error => console.log(error));
});
