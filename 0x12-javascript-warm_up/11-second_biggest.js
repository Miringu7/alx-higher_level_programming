#!/usr/bin/node


/*
 * script that prints “JavaScript is amazing”
 */

const args = process.argv.slice(2);

// Check if no arguments were passed or only one argument was passed
if (args.length === 0 || args.length === 1) {
    console.log(0);
} else {
    // Convert arguments to integers and sort them in descending order
    const integers = args.map(Number).sort((a, b) => b - a);

    // Find the second biggest integer
    const secondBiggest = integers[1];

    // Print the second biggest integer
    console.log(secondBiggest);
}

