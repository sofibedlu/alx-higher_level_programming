#!/usr/bin/node

const list = require('./100-data').list;

const indices = [];
const newList = list.map((x) => {
  const j = list.indexOf(x);
  if (j in indices) {
    indices.push(indices.length);
    return x * (indices.length);
  }
  indices.push(j);
  return x * list.indexOf(x);
});
console.log(list);
console.log(newList);
