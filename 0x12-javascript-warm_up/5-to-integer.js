#!/usr/bin/node

const { argv } = require('node:process');

if (Number(argv[2])) {
  console.log('My Number: ' + Number(argv[2]));
} else { console.log('Not a number'); }
