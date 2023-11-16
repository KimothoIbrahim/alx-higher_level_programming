#!/usr/bin/node

const n = Number(process.argv[2]);

function fact (n) {
  if (isNaN(process.argv[2]) || n === 1) return (1);
  return n * fact(n - 1);
}

console.log(fact(n));
