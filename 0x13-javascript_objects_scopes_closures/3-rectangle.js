#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    // Check if w or h is equal to 0 or not a positive integer
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // Create an empty object
      return {};
    }
    // Initialize the instance attribute width with the value of w
    this.width = w;
    // Initialize the instance attribute height with the value of h
    this.height = h;
  }

  // Instance method print() to print the rectangle using the character X
  print() {
    // Loop through each row
    for (let i = 0; i < this.height; i++) {
      // Create a string representing the row
      let row = '';
      // Loop through each column
      for (let j = 0; j < this.width; j++) {
        // Append 'X' to the row string
        row += 'X';
      }
      // Print the row
      console.log(row);
    }
  }
}

