# Detailed Bug Descriptions for Debugging Assignment

## Bug 1 – bug1.py
**Intended Behavior:** The script should calculate the average of a list of numbers and print the result.
**Issue Type:** Runtime Exception (ZeroDivisionError) and Type Error.
**Notes:** The program crashes when an empty list is processed due to division by zero, and it fails to concatenate a string with a float in the final print statement.

## Bug 2 – bug2.cpp
**Intended Behavior:** The program should perform basic arithmetic operations on values stored as strings after proper conversion and print the results.
**Issue Type:** Compilation Error (Type Mismatch).
**Notes:** Attempting to store the sum of two strings into an integer variable and multiplying a string by an integer without explicit conversion.

## Bug 3 – bug3.js
**Intended Behavior:** The function should extract and display a user's name, birth year, and theme color from a profile object.
**Issue Type:** Logical and Reference Error (TypeError).
**Notes:** The code tries to access a deeply nested property (`user.settings.theme.color`) on an object where the parent property is undefined, causing a crash.

## Bug 4 – bug4.c
**Intended Behavior:** The program should allocate memory for an array, populate it with values, and print them correctly.
**Issue Type:** Buffer Overflow and Memory Leak.
**Notes:** The loop index exceeds the allocated array limits (`i <= size`), and the dynamically allocated memory is never freed using `free()`.