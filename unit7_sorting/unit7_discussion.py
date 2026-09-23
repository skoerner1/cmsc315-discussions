"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a copy so the original list is not changed.
    sorted_list = lst.copy()

    # Move through the list multiple times.
    for i in range(len(sorted_list) - 1):

        # Track whether a swap happened during this pass.
        swapped = False

        # Compare adjacent values.
        for j in range(len(sorted_list) - 1 - i):

            # Swap values if they are in the wrong order.
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = \
                    sorted_list[j + 1], sorted_list[j]
                swapped = True

        # If no swaps occurred, the list is already sorted.
        if not swapped:
            break

    return sorted_list

def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # The list with 0 or 1 values is already sorted
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list
    middle = len(lst) // 2

    # Recursively divide and sort each half.
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    # Compare values from both lists.
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values.
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result



def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    dataset1 = [42, 17, 8, 63, 25, 91, 34, 12]

    print("Original List:   ", dataset1)
    print("Bubble Sort:     ", bubble_sort(dataset1))
    print("Merge Sort:      ", merge_sort(dataset1))
    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    dataset2 = [105, 54, 87, 23, 76, 11, 98, 45]

    print("Original List:   ", dataset2)
    print("Bubble Sort:     ", bubble_sort(dataset2))
    print("Merge Sort:      ", merge_sort(dataset2))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.


    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\nEmpty List:")
    print("Original:        ", empty_list)
    print("Bubble Sort:     ", bubble_sort(empty_list))
    print("Merge Sort:      ", merge_sort(empty_list))
    print("Both algorithms return an empty list because there are no values to sort.")

    # Edge Case 2: Already sorted list
    sorted_list = [10, 20, 30, 40, 50]

    print("\nAlready Sorted List:")
    print("Original:        ", sorted_list)
    print("Bubble Sort:     ", bubble_sort(sorted_list))
    print("Merge Sort:      ", merge_sort(sorted_list))
    print("The values remain in the same order because the list is already sorted.")

    # Edge Case 3: Duplicate values
    duplicate_list = [25, 10, 25, 5, 10, 30, 5]

    print("\nList With Duplicates:")
    print("Original:        ", duplicate_list)
    print("Bubble Sort:     ", bubble_sort(duplicate_list))
    print("Merge Sort:      ", merge_sort(duplicate_list))
    print("Both algorithms keep duplicate values while placing them in sorted order.")

    # ==================================
    # TODO (Student): Real World Example
    # ==================================

    print("\n=== REAL-WORLD SORTING EXAMPLE ===")

    # Satellite signal-strength readings measured in dBm.
    signal_strengths = [-82, -67, -91, -73, -58, -86, -64, -77]

    print("Satellite Signal Readings:", signal_strengths)
    print("Bubble Sort:              ", bubble_sort(signal_strengths))
    print("Merge Sort:               ", merge_sort(signal_strengths))

    print(
        "Sorting satellite signal readings can help organize received "
        "signal levels from weakest to strongest for analysis."
    )

if __name__ == "__main__":
    main()