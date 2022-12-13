#!/usr/bin/node
/*
 *Write a script that reads and prints the content of a file.
 */
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  const json = JSON.parse(body);
  let count = 0;
  const search = 'https://swapi-api.hbtn.io/api/people/18/';
  for (let value = 0; value < json.results.length; value++) {
    for (let i = 0; i < json.results[value].characters.length; i++) {
      if (json.results[value].characters[i].includes(search)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
