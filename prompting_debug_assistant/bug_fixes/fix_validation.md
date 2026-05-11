# Task 2 - Fix Validation Report

## Bug 1 - bug1_fixed.py
- **Test Case 1 (Standard)**:
    - **Input**: `data = [15, 25, 35, 45, 55]`
    - **Expected Output**: `Processing complete. Average score: 35.0`
    - **Actual Output**: `Processing complete. Average score: 35.0` ✅
- **Test Case 2 (Edge Case)**:
    - **Input**: `data = []`
    - **Expected Output**: `0`
    - **Actual Output**: `0` ✅
- **Note**: Fixed the `TypeError` by using f-string and handled `ZeroDivisionError` with an empty list check.

## Bug 2 - bug2_fixed.cpp
- **Test Case 1**:
    - **Input**: `part1 = "100"`, `part2 = "200"`
    - **Expected Output**: `Sum: 300`, `Product: 500`, `Status: Active`
    - **Actual Output**: `Sum: 300`, `Product: 500`, `Status: Active` ✅
- **Note**: Used `stoi()` to convert strings to integers and declared the missing `active_mode` variable.

## Bug 3 - bug3_fixed.js
- **Test Case 1**:
    - **Input**: `profileData` with missing `settings` object.
    - **Expected Output**: `Theme: default-blue` (no crash)
    - **Actual Output**: `Theme: default-blue` ✅
- **Note**: Implemented optional chaining (`?.`) to safely access nested properties and added default values for missing user data.

## Bug 4 - bug4_fixed.c
- **Test Case 1**:
    - **Input**: `size = 10`
    - **Expected Output**: Successful execution and all 10 indices printed without memory errors.
    - **Actual Output**: Printed indices 0 to 9 correctly. ✅
- **Note**: Fixed the off-by-one error in the loop (`i < size`) and added `free(array)` to prevent memory leaks.