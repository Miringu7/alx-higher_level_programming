#!/usr/bin/node


/*
 * script that prints “JavaScript is amazing”
 */

const printArguments = () => {
    // Check if there are at least two arguments passed
    if (process.argv.length >= 4) {
        // Print the first and second arguments passed to the script in the specified format
        console.log(process.argv[2] + " is " + process.argv[3]);
    } else {
        // Print an error message if there are not enough arguments
        console.log("Please provide at least two arguments.");
    }
};

// Call the function
printArguments();

