#!/usr/bin/node

const fs = require('fs');

const fileOnePath = process.argv[2];
const fileOneContent = fs.existsSync(fileOnePath) ? fs.readFileSync(fileOnePath, 'utf8') : '';

const fileTwoPath = process.argv[3];
const fileTwoContent = fs.existsSync(fileTwoPath) ? fs.readFileSync(fileTwoPath, 'utf8') : '';

const concatenatedContent = fileOneContent + fileTwoContent;

const destinationPath = process.argv[4];
fs.writeFileSync(destinationPath, concatenatedContent);

console.log(`Concatenated files '${fileOnePath}' and '${fileTwoPath}' to '${destinationPath}'`);
