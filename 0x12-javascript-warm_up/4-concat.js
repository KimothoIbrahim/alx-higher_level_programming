#!/usr/bin/node

const { argv } = require('node:process');
const myVar = ' is ';

console.log(argv[2] + myVar + argv[3]);
