#!/usr/bin/node
/* searches the second biggest integer in the list of arguments */

let maximum = 0;
let secondMax = 0;
for (const num of process.argv.slice(2).map(Number)) {
  if (num > maximum) {
    secondMax = maximum;
    max = num;
  }
  if (num > secondMax && maximum > num) {
    secondMax = num;
  }
}
console.log(secondMax);
