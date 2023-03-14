#!/usr/bin/node

exports.esrever = function (list) {
  let temp;
  let size = list.length;
  for (let i = 0; i < (list.length) / 2; i++) {
    temp = list[i];
    list[i] = list[--size];
    list[size] = temp;
  }
  return list;
};
