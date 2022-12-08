#!/usr/bin/node
/*
Write a script that prints 3 lines:”:
*/

const arg = process.argv[2];
if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
