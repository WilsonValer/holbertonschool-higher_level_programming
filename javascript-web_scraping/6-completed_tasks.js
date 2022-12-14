#!/usr/bin/node
/*
 * prints the number of movies where the character "Wedge Antilles" is present
 */

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const userTasks = {};
    data.forEach(function (task) {
      if (task.completed) {
        const userId = task.userId;
        if (userTasks[userId]) {
          userTasks[userId] += 1;
        } else {
          userTasks[userId] = 1;
        }
      }
    });
    console.log(userTasks);
  }
});
