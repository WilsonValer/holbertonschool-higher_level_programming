#!/usr/bin/node
/*
*Write a class Rectangle that defines a rectangle:
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
