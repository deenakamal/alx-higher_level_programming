#!/usr/bin/node

const dict = require('./101-data').dict;
const mDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (mDict[value] === undefined) {
    mDict[value] = [key];
  } else {
    mDict[value].push(key);
  }
}
console.log(mDict);
