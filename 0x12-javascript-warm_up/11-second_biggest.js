#!/usr/bin/node

const n = process.argv;

if (process.argv[2]) {
  if (!process.argv[3]) {
    console.log('0');
  } else {
    let y = Number(n[2]);
    for (let x = 2; x < n.length; x++) {
      if (Number(n[x]) > y) {
        y = Number(n[x]);
      }
    }

    let z = Number(n[2]);
    for (let x = 2; x < n.length; x++) {
      if (Number(n[x]) > z && Number(n[x]) < y) {
        z = Number(n[x]);
      }
    }

    console.log(z);
  }
} else {
  console.log('0');
}
