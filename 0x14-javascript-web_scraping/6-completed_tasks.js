#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  const obj = {};
  let task = 0;
  for (let id = 1; id <= 10; id++) {
    for (const user of data) {
      if (user.userId === id && user.completed === true) {
        task++;
      }
    }
    obj[`${id}`] = task;
    task = 0;
  }
  console.log(obj);
});
