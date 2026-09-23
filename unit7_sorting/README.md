# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Code Implementation

- This program utilizes Bubble Sort and Merge Sort to demonstrate two 
different methods of sorting data.
- I created two unsorted datasets and used both algorithms to arrange 
the values from lowest to highest.
- I implemented Bubble Sort by comparing adjacent values and swapping them 
when they were out of order.
- I implemented Merge Sort by recursively dividing the list into smaller 
sections and merging them back together in sorted order.
- I tested three edge cases using an empty list, an already sorted list, 
and a list containing duplicate values.
- I created a real-world example using satellite signal-strength readings 
measured in dBm and sorted the readings from weakest to strongest.

## Discussion Board Reflection

I learned that Bubble Sort works by making repeated passes through the data 
and moving values into the correct position through comparisons and swaps. 
Merge Sort takes a completely different approach by breaking the problem into
smaller pieces and then rebuilding the list in sorted order. The most 
challenging part for me was understanding how Merge Sort keeps track of the 
smaller lists during recursion. After working through the code and comparing 
the final results from multiple datasets, the process started to make more 
sense. Bubble Sort is straightforward and can work well when there are only
a small number of values, but its O(n²) complexity becomes a disadvantage as 
the amount of data increases. Merge Sort performs at O(n log n), making it 
more practical for larger datasets, although it uses additional memory. This 
assignment showed me that choosing a sorting method depends on both the data 
being processed and the efficiency needed.