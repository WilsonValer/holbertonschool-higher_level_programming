#!/usr/bin/node
/*
 * prints the number of movies where the character "Wedge Antilles" is present
 */
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) throw err;
    });
  }
});
