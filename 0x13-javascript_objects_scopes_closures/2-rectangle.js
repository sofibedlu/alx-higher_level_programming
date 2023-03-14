#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === 0 || !Number.isInteger(w) || w < 0 ||
         h === 0 || !Number.isInteger(h) || h < 0) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
