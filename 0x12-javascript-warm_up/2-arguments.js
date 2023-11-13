#!/usr/bin/node

const {argv} = require('node:process');

if (argv[3])
{
	console.log('Arguments found');
	return;
}

if (argv[2])
{
	console.log('Argument found');
}else
	console.log('No argument');
