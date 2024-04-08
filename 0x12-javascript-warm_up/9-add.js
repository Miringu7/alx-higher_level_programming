#!/usr/bin/node


/*
 * script that prints “JavaScript is amazing”
 */

const add = (a, b) => {
    return a + b;
};

// Get the first and second integers from the command line arguments
const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

// Check if both arguments are valid integers
if (!isNaN(firstInteger) && !isNaN(secondInteger)) {
    // Call the add function and print the result
    console.log(add(firstInteger, secondInteger));
} else {
    // Print an error message if any argument couldn't be converted to an integer
    console.log("Invalid arguments. Please provide two integers.");
}

