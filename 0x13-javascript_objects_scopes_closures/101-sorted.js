#!/usr/bin/node
const dict = require('./101-data.js').dict;

const dict1 = {};
for (const [k, v] of Object.entries(dict)) {
  // console.log(k, v);
  if (!dict1[v]) {
    dict1[v] = [k];
    continue;
  }
  // console.log(dict1[v]);
  dict1[v] = dict1[v].concat(k);
}

console.log(dict1);
