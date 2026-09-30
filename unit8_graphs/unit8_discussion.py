"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Return an empty list if the starting device
    # does not exist in the network.
    if start not in graph:
        return []

    visited = set()

    # BFS uses a queue because the first device discovered
    # should be the first device explored.
    queue = deque([start])

    traversal_order = []

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            # Add connected devices to the queue so BFS
            # can explore the network level by level.
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    network = {
        "Router": ["Switch 1", "Switch 2"],
        "Switch 1": ["Router", "Computer 1", "Computer 2"],
        "Switch 2": ["Router", "Server", "Access Point"],
        "Computer 1": ["Switch 1"],
        "Computer 2": ["Switch 1"],
        "Server": ["Switch 2"],
        "Access Point": ["Switch 2"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    for device, connections in network.items():
        print(device, "->", connections)

    print("\n=== BFS TRAVERSAL ===")

    start_device = "Router"

    print("Starting device:", start_device)
    print("Traversal order:", bfs(network, start_device))

    # A network printer is added to the graph.
    # The printer is connected directly to Switch 1.

    network["Printer"] = ["Switch 1"]
    network["Switch 1"].append("Printer")

    print("\n=== UPDATED GRAPH ===")
    print("Added Printer connected to Switch 1.")

    # Display the updated graph.
    for device, connections in network.items():
        print(device, "->", connections)

    print("\nUpdated BFS traversal:")
    print(bfs(network, "Router"))


    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1:
    # Start BFS from a different device.
    # The traversal order changes because BFS now
    # explores outward from Computer 1.

    print("\nEdge Case 1: Different starting device")
    print("Starting from Computer 1:")
    print(bfs(network, "Computer 1"))

    # Edge Case 2:
    # Attempt to start from a device that does not
    # exist in the network. The function safely
    # returns an empty list.

    print("\nEdge Case 2: Missing starting device")
    print("Starting from Unknown Device:")
    print(bfs(network, "Unknown Device"))

    # Edge Case 3:
    # Test a graph containing only one device.
    # BFS should visit only that device.

    single_device_network = {
        "Router": []
    }

    print("\nEdge Case 3: Single-device network")
    print(bfs(single_device_network, "Router"))



if __name__ == "__main__":
    main()