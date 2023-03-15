#!/usr/bin/node

const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
const file1C = fs.readFileSync(`${file1}`, 'utf-8');
const file2C = fs.readFileSync(`${file2}`, 'utf-8');
const newF = file1C + file2C;
fs.writeFileSync(`${file3}`, newF, 'utf-8');
