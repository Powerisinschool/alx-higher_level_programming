#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;

      for (; j < this.width; ++j) {
        process.stdout.write('X');
      }

      if (j === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
