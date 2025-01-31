#!/usr/bin/node
/* searches the second biggest integer in the list of arguments */
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = parseInt(args[2]);
  let secondMax = parseInt(args[3]);

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
