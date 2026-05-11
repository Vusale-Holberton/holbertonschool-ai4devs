# Bug Reports

## Bug Report - bug1.py
- **Summary**: Off-by-one error in slicing logic during list processing.
- **Root Cause**: The code used `items[len(items)-n-1]` which subtracted an extra index, leading to incorrect element selection.
- **Resolution**: Updated the slicing logic to `items[len(items)-n:]` to correctly capture the last N elements.
- **Lesson Learned**: Always test edge cases with minimal input and verify index boundaries.

## Bug Report - bug2.cpp
- **Summary**: Memory leak due to unreleased dynamic memory in the matrix calculation loop.
- **Root Cause**: The `new` keyword was used to allocate memory for an array, but the corresponding `delete[]` was missing at the end of the function.
- **Resolution**: Added `delete[] matrix;` before the return statement to ensure proper memory deallocation.
- **Lesson Learned**: Utilize RAII patterns or smart pointers in C++ to manage resource lifecycles automatically.

## Bug Report - bug3.js
- **Summary**: Asynchronous race condition when fetching user data.
- **Root Cause**: The function was not using `await` for the database call, causing the response to be sent before data was retrieved.
- **Resolution**: Converted the function to `async` and added the `await` keyword to the fetch operation.
- **Lesson Learned**: Always handle Promises correctly to ensure execution order in non-blocking environments.

## Bug Report - bug4.c
- **Summary**: Segmentation fault caused by accessing a NULL pointer.
- **Root Cause**: The code did not check if `malloc()` successfully allocated memory before writing to the pointer.
- **Resolution**: Added a NULL check immediately after allocation and handled the error gracefully.
- **Lesson Learned**: Defensive programming is essential in C; always validate pointers before dereferencing.