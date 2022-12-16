#!/usr/bin/node


const request = require('request');
request(process.argv[2], function (error, response, body) {

  if (!error) {
    const todos = JSON.parse(body);
    const t1 = {};
    todos.forEach((todo) => {
      if (todo.completed && t1[todo.userId] === undefined) {
        t1[todo.userId] = 1;
      } else if (todo.completed) {
        t1[todo.userId] += 1;
      }
    });
    console.log(t1);
  }
})
