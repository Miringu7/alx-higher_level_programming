#!/usr/bin/node


/*
 * script that prints “JavaScript is amazing”
 */

const x = parseInt(process.argv[2]);

// Check if the conversion resulted in a valid integer
if (!isNaN(x)) {
    // Loop x times and print "C is fun" each time
    for (let i = 0; i < x; i++) {
        console.log("C is fun");
    }
} else {
    // Print an error message if the first argument couldn't be converted to an integer
    console.log("Missing number of occurrences");
}

