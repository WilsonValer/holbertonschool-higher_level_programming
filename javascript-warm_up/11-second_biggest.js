#!/usr/bin/node
/*
 * Write a script that prints two arguments passed to it, in the following format: “ is ”
*/

const process = require('process');

const list = process.argv.slice(2);
const newList = list.map(i => parseInt(i));

function nextBiggest (newList) {
  let max = 0;
  let result = 0;

  for (const value of newList) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr]; // save previous max
    } else if (nr < max && nr > result) {
      result = nr; // new second biggest
    }
  }

  return result;
}

console.log(nextBiggest(newList));
