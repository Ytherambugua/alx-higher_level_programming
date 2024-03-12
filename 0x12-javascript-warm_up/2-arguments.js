#!/usr/bin/node
// Using process.argv to access command line arguments
const argsCount = process.argv.length;
// Checking number of arguments and printing the messages accordingly
if (argsCount === 2) {
	console.log('No argument');
} else if (argsCount === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
