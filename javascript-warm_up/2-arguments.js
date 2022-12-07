#!/usr/bin/node
/*
Write a script that prints 3 lines:”:
*/

const myArgv = process.argv.slice(2);

const large = myArgv.length;
if (large >= 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
