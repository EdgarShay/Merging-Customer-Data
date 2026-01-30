# Customer Data Merge – Technical Interview Preparation

## Overview
This project simulates a real-world data analytics scenario where customer data from multiple sources must be consolidated.
The goal is to merge two sorted datasets of customer IDs into a single sorted dataset, ensuring optimal performance and clarity.

This solution was developed as part of a technical interview preparation assignment for a data analytics company specializing in market research.

## Solution Approach
- The merge is performed from the end of the array to avoid overwriting valid data.
- Three pointers are used:

  - Pointer for the last valid element in `customerData1`
  - Pointer for the last element in `customerData2`
  - Pointer for the final merge position
- This approach reflects efficient data consolidation techniques used in production systems.

------

## Diagram / Flowchart
A visual diagram illustrating the pointer-based merge strategy is included in the `diagrams/` folder.

------

## Test Cases
Automated unit tests were written using Python’s built-in `unittest` framework.

## Test Coverage
Normal cases:
- Merging two populated datasets
- Interleaved customer IDs
- Reverse-order dominance

Edge cases:
- Empty second dataset
- Empty first dataset
- Duplicate customer IDs


## Problem Statement
Given:
- Two integer arrays `customerData1` and `customerData2`, sorted in non-decreasing order
- Integers `m` and `n` representing the number of valid customer records in each array

Constraints:
- `customerData1` has a length of `m + n`
- The last `n` elements of `customerData1` are placeholders (`0`)
- The final merged dataset must be stored inside `customerData1`

