#!/usr/bin/node
const Square5 = require('./5-square.js');

module.exports = class Square extends Square5 {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c || 'X');
      }
      console.log('');
    }
  }
};
