#!/usr/bin/node

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const request = require('request');

request(url, (error, response, body) => {
  const info = JSON.parse(body);
  const characters = info.characters;

  for (character of characters) {
    request(character, (err, response, body) => {
      const info = JSON.parse(body);
      console.log(info.name);
    });
  }
});
