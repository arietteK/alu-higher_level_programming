#!/usr/bin/node
/* prints the addition of 2 integers */
const num1 = process.argv[2];
const num2 = process.argv[3];

function add (a, b) {
    return a + b;
}

const a = parseInt(num1);
const b = parseInt(num2);
console.log(add(a, b));
