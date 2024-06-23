#!/usr/bin/node

fs = require('fs');

try {
  fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) {
      console.error('The was an error reading the file! :', err);
      return;
    }
    console.log('The supplied file contains the following content:', data);
  });
} catch (err) { console.log(err); }
