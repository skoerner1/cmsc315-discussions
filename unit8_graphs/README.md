# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.

## Code Implementation

- I represented a small computer network as a graph where each
device is a node and the connections between devices are edges.
- I used an adjacency list to store which devices are directly
connected to one another within the network.
- I performed BFS starting at the router and used a queue to
control the order in which the network devices were explored.
- I used a set to keep track of devices that had already been
visited so the program would not repeatedly process the same 
connection.
- I modified the original graph by adding a printer to Switch 1
and then ran BFS again to observe the change in traversal 
order.
- I tested the program from Computer 1 to demonstrate how 
selecting a different starting point affects the order of 
the traversal.
- I also tested a missing device and a single-device network 
to make sure the BFS function handled unusual situations
correctly.

## Discussion Board Reflection

When I started this assignment, I understood that devices could be 
represented as nodes, but implementing BFS helped me see how those 
connections are actually followed during a traversal. I also gained
a better understanding of using a queue and a visited set together.
The queue controls which device is checked next, while the visited 
set prevents the program from repeatedly processing the same 
devices. One challenge was making sure connected devices did not
cause the traversal to loop back and forth. Tracking the visited
nodes helped solve this problem, and testing from different
starting devices showed me that the results were working correctly.
BFS and DFS have different approaches to navigating a graph. BFS
works outward from the starting point and checks connections by
level, while DFS continues down a path before returning to explore
other options. In networking, BFS could help discover devices or 
determine connection paths. DFS could be useful when examining 
individual network paths or troubleshooting connections through 
multiple devices.


