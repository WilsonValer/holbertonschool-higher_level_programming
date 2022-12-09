#!/usr/bin/node
/*
 * Write a script that prints two arguments passed to it, in the following format: “ is ”
*/

const argv = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i <= process.argv.length; i++) {
  console.log(argv[i]);
}
