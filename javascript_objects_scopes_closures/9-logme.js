#!/usr/bin/node
/*
*Write a function that prints the number of arguments
*already printed and the new argument value. (see example below)
*/
let number = 0;
exports.logMe = function (item) {
  console.log(number + ': ' + item);
  number += 1;
};
