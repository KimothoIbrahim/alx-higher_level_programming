#!/usr/bin/node

let i = 3;
let j = 3;
let biggest = process.argv[2];
let secondBiggest = biggest;

while (process.argv[i]) {
  if (process.argv[i] > biggest) { biggest = process.argv[i]; }
  i++;
}
while (process.argv[j]) {
  if (process.argv[j] > secondBiggest && process.argv[j] < biggest) { secondBiggest = process.argv[j]; }
  j++;
}

if (!process.argv[3]) { console.log(0); } else { console.log(secondBiggest); }
