#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
