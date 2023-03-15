#!/usr/bin/node

function factorial (value) {
  if (value === 1) {
    return 1;
  }
  return value * factorial(value - 1);
}
const num = process.argv[2];
if (isNaN(num)) {
  console.log(1);
} else {
  const facto = factorial(parseInt(num));
  console.log(facto);
}
