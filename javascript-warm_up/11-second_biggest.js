#!/usr/bin/node
/* searches the second biggest integer in the list of arguments */
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = 0;
  let secondMax = 0;

  for (const num of args) {
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
