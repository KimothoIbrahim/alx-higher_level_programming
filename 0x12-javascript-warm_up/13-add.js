#!/usr/bin/node

exports.add = function (a, b) {
  if (Number(a) && Number(b)) {
    return a + b;
  } else {
    console.log('Use valid numbers');
  }
};
