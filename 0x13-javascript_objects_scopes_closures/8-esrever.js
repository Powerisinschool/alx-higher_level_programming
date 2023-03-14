#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  while (i < j) {
    // swap list[i] and list[j]
    let temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    // increment i and decrement j
    i++;
    j--;
  }
  return list;
}
