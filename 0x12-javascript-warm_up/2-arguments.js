#!/usr/bin/node


/*
 * script that prints a message depending of the number of arguments passed”
 */

const printMessage = () => {
    // Check the number of arguments passed
    switch (process.argv.length)
	{
        case 2:
            console.log("No argument");
            break;
        case 3:
            console.log("Argument found");
            break;
        default:
            console.log("Arguments found");
    }
};

// Call the function
printMessage();

