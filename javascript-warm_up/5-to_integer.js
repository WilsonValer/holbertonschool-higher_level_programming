#!/usr/bin/node
/*
 * Write a script that prints two arguments passed to it, in the following format: “ is ”
*/

const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
