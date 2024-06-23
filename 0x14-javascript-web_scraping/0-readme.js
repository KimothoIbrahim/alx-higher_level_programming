#!/usr/bin/node

fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error('The was an error reading the file! :', err);
    return;
  }
  console.log('The supplied file contains the following content:', data);
});
