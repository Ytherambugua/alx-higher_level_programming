#!/usr/bin/node
// Command line arguments
const arg = process.argv[2];
// Checking the arguments if tey were passed or not
if (arg === undefined) {
        	console.log('No argument');
} else {
	        console.log(arg);
}
