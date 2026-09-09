# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Code Implementation

- This program compared linear search and binary search using small
and large datasets. 
- I implemented both algorithms and tested values that existed and 
did not exist. 
- I used GOES satellite IDs for the small dataset and satellite tracking 
records for the large dataset.
- I tested edge cases including an empty list, a single-element list, and values 
at the first and last positions. Both algorithms returned the correct results. 
Linear search checked values one at a time, while binary search reduced the 
search area by half. Binary search was more efficient for larger sorted datasets.
- I created a satellite ground station scenario that searched GOES satellite IDs to 
determine if a specific satellite was in the system.

## Discussion Board Reflection
This assignment helped me better understand the difference between linear search and
binary search and how each one searches through data. I learned how the size of a 
dataset can make choosing the right search algorithm more important. One challenge 
I had was understanding how binary search keeps changing the low, high, and middle 
values to find the target. Running the program with different satellite IDs and 
looking at the results helped me understand how the search area gets smaller each 
time. Testing the edge cases also helped me make sure the algorithms worked correctly
with different situations. I utilized linear search when working with a smaller 
dataset or data that is not sorted. I think Binary search would be a better choice 
for a large sorted dataset because it does not have to check every value. The 
tradeoff is that binary search requires the data to be sorted first, while linear 
search does not.