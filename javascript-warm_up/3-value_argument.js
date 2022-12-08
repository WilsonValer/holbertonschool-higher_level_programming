#!/usr/bin/node
/*
Write a script that prints 3 lines:”:
*/

// const myArgv = process.argv.slice(2);
/*
for(var i = 2; i < process.argv.length; i++) {
  console.log(process.argv[i]);
}
*/
const arg = process.argv[2];
if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
