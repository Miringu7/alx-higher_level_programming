#!/usr/bin/node


/*
 * script that prints “JavaScript is amazing”
 */

const size = parseInt(process.argv[2]);

// Check if the conversion resulted in a valid integer
if (!isNaN(size)) {
    // Loop through each row
    for (let i = 0; i < size; i++) {
        let row = "";
        // Loop through each column in the row
        for (let j = 0; j < size; j++) {
            row += "X"; // Add X character to the row
        }
        console.log(row); // Print the row
    }
} else {
    // Print an error message if the first argument couldn't be converted to an integer
    console.log("Missing size");
}

