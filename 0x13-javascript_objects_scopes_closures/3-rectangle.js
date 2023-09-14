#!/usr/bin/node

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let prints = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        prints = prints + 'X';
      }
      console.log(prints);
      prints = '';
    }
  }
};

module.exports = Rectangle;
