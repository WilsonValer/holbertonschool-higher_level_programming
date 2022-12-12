#!/usr/bin/node
/*
 *Write a script that reads and prints the content of a file.
 */
const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];
fs.writeFile(file, data, (err) => {
  if (err) throw err;
  console.log('Exitoso');
});
