#!/usr/bin/node

const count = process.argv.length - 2;

if (count <= 1) {
  console.log(0);
} else {
  const numericCount = process.argv.slice(2).map(Number);
  const sortedArr = numericCount.sort((a, b) => b - a);
  console.log(sortedArr[1]);
}
