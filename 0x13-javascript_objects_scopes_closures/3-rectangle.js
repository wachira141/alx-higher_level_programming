#!/usr/bin/node
module.exports = class Rectangle {
	constructor (w, h) {
		if (w >0 && h > 0) {
			this.weight = w;
			this.height = h;
		}
	}
	print() {
		for (let column = 0; column < this.height; column += 1) {
			console.log('X'.repeat(this.width));
		}
	}
};
