#!/usr/bin/node


// Using arrow function to define the function

const printFirstArgument = () => {
    // Check if arguments array is empty
    if (!process.argv[2]) {
        console.log("No argument");
    } else {
        // Print the first argument passed to the script
        console.log(process.argv[2]);
    }
};

// Call the function
printFirstArgument();

