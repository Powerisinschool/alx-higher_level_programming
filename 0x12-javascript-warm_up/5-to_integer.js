#!/usr/bin/node
const n = process.argv[2];
if (!Number(n)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(n));
}
