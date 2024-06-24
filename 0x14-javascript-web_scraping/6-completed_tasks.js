#!/usr/bin/node

const request = require('request'); const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body).filter((todo) => todo.completed);

    const ob = {};

    for (let i = 1; i < 11; i++) {
      const count = info.filter((todo) => { return todo.userId === i; });
      if (count) {
        ob[i] = count.length;
      }
    }
    console.log(ob);
  } else (console.log(error));
});
