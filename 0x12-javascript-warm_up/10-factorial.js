#!/usr/bin/node


/*
 * script that prints “JavaScript is amazing”
 */

const factorial = (n) => {
    // Base case: factorial of 0 or NaN is 1
    if (isNaN(n) || n === 0) {
        return 1;
    }
    // Recursive case: compute factorial by multiplying n with factorial of (n-1)
    else {
        return n * factorial(n - 1);
    }
};

// Get the integer argument from the command line
const integerArg = parseInt(process.argv[2]);

// Compute and print the factorial
console.log(factorial(integerArg));

