#!/usr/bin/node

const request = require('request'); const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    let count = 0;
    const info = JSON.parse(body);
    for (movie of info.results) {
      for (character of movie.characters) {
        if (character.endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
