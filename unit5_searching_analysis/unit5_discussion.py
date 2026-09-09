"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    - It has O(n) time complexity because
      every element in the list must be checked.
    """
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:

        # Find the middle position of search area.
        middle = (low + high) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:
            low = middle + 1

        else:
            high = middle - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    goes_satellites = [14, 15, 16, 17, 18, 19]

    print("GOES Satellite IDs:", goes_satellites)

    # Search for a value that exists.
    target = 17

    print("\nSearching for GOES", target)
    print("Linear Search Index:",
        linear_search(goes_satellites, target))
    print("Binary Search Index:",
        binary_search(goes_satellites, target))

    # Both algorithms should return index 3 because
    # GOES 17 is located at index 3.

    # Search for a value that does not exist.
    target = 20

    print("\nSearching for GOES", target)
    print("Linear Search Index:",
        linear_search(goes_satellites, target))
    print("Binary Search Index:",
        binary_search(goes_satellites, target))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    tracking_records = list(range(1, 10001))

    target = 9999

    print("Number of Tracking Records:", len(tracking_records))
    print("Searching for Tracking Record:", target)

    print("Linear Search Index:",
      linear_search(tracking_records, target))

    print("Binary Search Index:",
        binary_search(tracking_records, target))
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.
    
    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\nEdge Case 1 - Empty List")

    print("Linear Search:",
      linear_search(empty_list, 16))

    print("Binary Search:",
        binary_search(empty_list, 16))


    # Edge Case 2: Single-element list
    single_satellite = [16]

    print("\nEdge Case 2 - Single Satellite")

    print("Linear Search:",
        linear_search(single_satellite, 16))

    print("Binary Search:",
        binary_search(single_satellite, 16))

    # Edge Case 3: First position
    print("\nEdge Case 3 - First Satellite")

    print("Searching for GOES 14")

    print("Linear Search:",
      linear_search(goes_satellites, 14))

    print("Binary Search:",
        binary_search(goes_satellites, 14))


    # Edge Case 4: Last position
    print("\nEdge Case 4 - Last Satellite")

    print("Searching for GOES 19")

    print("Linear Search:",
        linear_search(goes_satellites, 19))

    print("Binary Search:",
        binary_search(goes_satellites, 19))

    # ===============================
    # REAL-WORLD SEARCH SCENARIO
    # ===============================
    # A satellite ground station may track multiple
    # satellites. A search algorithm could be used to
    # determine whether a specific satellite ID is
    # contained in the ground station's system.

    print("\n=== REAL-WORLD SEARCH SCENARIO ===")

    ground_station_satellites = [14, 15, 16, 17, 18, 19]

    target_satellite = 18

    print("Ground Station Satellite IDs:",
        ground_station_satellites)

    print("Searching for GOES", target_satellite)

    result = binary_search(
        ground_station_satellites,
        target_satellite
    )

    if result != -1:
        print(
            "GOES",
            target_satellite,
            "was found at index",
            result
        )
    else:
        print(
            "GOES",
            target_satellite,
            "was not found."
        )


if __name__ == "__main__":
    main()