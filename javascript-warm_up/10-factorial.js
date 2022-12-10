#!/usr/bin/node
/*
 * Write a script that prints two arguments passed to it, in the following format: “ is ”
*/

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(n));
