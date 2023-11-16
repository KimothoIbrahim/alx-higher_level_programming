#!/usr/bin/node

if (!Number(process.argv[2])) {
  console.log('Missing size');
}

for (let a = 0; a < Number(process.argv[2]); a++) {
  console.log('X'.repeat(Number(process.argv[2])));
}
