#!/usr/bin/node
const num = parseFloat(process.argv[2]);
if (isNan(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(num)}`);
}
