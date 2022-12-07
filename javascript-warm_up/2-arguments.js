#!/usr/bin/node
/*
Write a script that prints 3 lines:”:
*/

const myArgv = process.argv.slice(2);

const large = myArgv.length;
if (large === 0) {
  console.log('No argument');
} else if (large === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
