#!/usr/bin/node

const { list } = require('./100-data');
const newList = list.map(function (x) {
  return x * list.indexOf(x);
});
console.log(list);
console.log(newList);
