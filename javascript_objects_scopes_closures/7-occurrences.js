#!/usr/bin/node
/*
*Write a class Rectangle that defines a rectangle:
*/

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(number => {
    if (number === searchElement) {
      count += 1;
    }
  });
  return count;
};
