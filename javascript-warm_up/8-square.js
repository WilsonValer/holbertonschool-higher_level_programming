#!/usr/bin/node
/*
 * Write a script that prints two arguments passed to it, in the following format: “ is ”
*/

const num = parseInt(process.argv[2]);
if (isNaN(num)) console.log('Missing size');
else {
  let v = '';
  for (let i = 0; i < num; i++) v += 'X';
  v.split('').forEach(() => console.log(v));
}
