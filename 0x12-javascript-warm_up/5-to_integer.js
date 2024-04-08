#!/usr/bin/node


/*
 * script that prints “JavaScript is amazing”
 */

const printNumber = () => {
    // Convert the first argument to an integer
    const number = parseInt(process.argv[2]);

    // Check if the conversion resulted in a valid integer
    if (!isNaN(number)) {
        // Print the number if it's a valid integer
        console.log(`My number: ${number}`);
    } else {
        // Print "Not a number" if the conversion failed
        console.log("Not a number");
    }
};

// Call the function
printNumber();

