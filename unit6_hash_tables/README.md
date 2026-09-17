# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Code Implementation

- This program utilizes a Python dictionary to demonstrate how a hash table stores 
information as key-value pairs.
- I created a tool inventory with tool IDs as the keys and tool names as the values.
- I utilized lookup operations by using specific tool IDs to retrieve the tools associated 
with them.
- I updated an existing tool from a Torque Wrench to a Digital Torque Wrench and deleted 
the Circular Saw from the dictionary.
- I tested edge cases by looking up a tool ID that did not exist and safely attempting 
to delete a missing tool ID. Both operations returned "Tool not found" without causing 
an error.
- I created a real-world tool inventory scenario that could be used to quickly locate 
and manage tools based on their unique ID numbers.

## Discussion Board Reflection

When conducting this discussion project, I learned that each value in a dictionary is 
connected to a unique key, which makes it easy to find a specific piece of information. 
Working with the tool inventory helped me practice adding new entries, searching for tools, 
changing an existing value, and removing an entry. I also learned how to handle situations 
where a key is not found without causing the program to stop. One challenge I encountered 
was understanding how hashing works compared to other methods of storing and searching data. 
Going through each dictionary operation helped make the concept easier to understand. A hash 
table uses a hash function to determine where data should be stored. Sometimes two different 
keys can end up being assigned to the same location, which is known as a collision. Hash 
tables have ways of handling these collisions while keeping the data accessible. They can 
improve efficiency because the program can use a key to access information directly instead 
of searching through each entry in order.
