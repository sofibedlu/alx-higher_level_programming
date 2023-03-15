#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const subArray = process.argv.slice(2);
  const newArray = subArray.map(function (x) {
    return parseInt(x);
  });

  let temp;
  for (let i = 0; i < newArray.length; i++) {
    for (let j = 0; j < newArray.length - 1; j++) {
      if (newArray[j] > newArray[j + 1]) {
        temp = newArray[j];
        newArray[j] = newArray[j + 1];
        newArray[j + 1] = temp;
      }
    }
  }
  console.log(newArray[newArray.length - 2]);
}
