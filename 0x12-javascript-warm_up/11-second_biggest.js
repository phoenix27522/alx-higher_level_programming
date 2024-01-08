#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // Get arguments and convert to numbers
const sortedArgs = args.sort((a, b) => b - a); // Sort arguments in descending order

if (sortedArgs.length <= 1) {
  console.log(0);
} else {
  const secondBiggest = sortedArgs[1];
  console.log(secondBiggest);
}
