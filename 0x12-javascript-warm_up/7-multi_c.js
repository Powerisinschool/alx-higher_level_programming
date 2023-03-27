#!/usr/bin/node
let n = process.argv[2];
if (!Number(n)) {
  console.log('Missing number of occurrences');
} else {
  n = parseInt(n);
  for (let i = 0; i < n; i++) console.log('C is fun');
}
