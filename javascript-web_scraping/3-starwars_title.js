#!/usr/bin/node
/*
 *Write a script that reads and prints the content of a file.
 */
const request = require('request');
const titleId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
const urlId = `${url}${titleId}`;
request(urlId, (error, response, body) => {
  if (error) console.log(error);
  const json = JSON.parse(body);
  console.log(json.title);
});
