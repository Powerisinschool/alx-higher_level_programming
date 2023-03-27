#!/usr/bin/node
const fs = require('fs');

const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];

const file1 = fs.readFileSync(f1).toString();
const file2 = fs.readFileSync(f2).toString();
const file3 = file1 + file2;

fs.writeFile(f3, file3, err => {
  if (err) {
    console.error(err);
  }
});
