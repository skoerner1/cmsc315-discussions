"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    lst.insert(index, value)


def delete_at(lst, index):
    if 0 <= index < len(lst):
        return lst.pop(index)
    return None


def search_value(lst, value):
    for index in range(len(lst)):
        if lst[index] == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    # This list is a list of equipment that is utilized in satellite tracking.
    equipment = ["LNA", "Upconverter", "Spectrum Analyzer", "SSPA"]
    print("\n=== INSERTION TESTS ===")
    print("Original equipment list:", equipment)

    # Insert equipment at the beginning of the list.
    insert_at(equipment, 0, "Antenna Control Unit")
    print("After inserting at the beginning:", equipment)

    # Insert equipment in the middle of the list.
    middle_index = len(equipment) // 2
    insert_at(equipment, middle_index, "Downconverter")
    print("After inserting in the middle:", equipment)

    # Insert equipment at the end of the list.
    insert_at(equipment, len(equipment), "Power Supply")
    print("After inserting at the end:", equipment)

    print("\n=== DELETION TESTS ===")
    # Remove the first item in the list.
    removed = delete_at(equipment, 0)
    print("Removed from the beginning:", removed)
    print("Updated list:", equipment)

    # Remove an item from the middle of the list.
    middle_index = len(equipment) // 2
    removed = delete_at(equipment, middle_index)
    print("Removed from the middle:", removed)
    print("Updated list:", equipment)

    # Remove the last item in the list.
    removed = delete_at(equipment, len(equipment) - 1)
    print("Removed from the end:", removed)
    print("Updated list:", equipment)

    print("\n=== SEARCH TESTS ===")
    # Search for equipment that exists in the list.
    search_item = "LNA"
    result = search_value(equipment, search_item)

    if result != -1:
        print(search_item, "was found at index", result)
    else:
        print(search_item, "was not found.")

    # Search for equipment that does not exist in the list.
    search_item = "GPS Receiver"
    result = search_value(equipment, search_item)

    if result != -1:
        print(search_item, "was found at index", result)
    else:
        print(search_item, "was not found.")

    print("\n=== EDGE CASES ===")
    # Edge Case 1
    removed = delete_at(equipment, 100)
    print("Attempting to delete at invalid index:", removed)

    # Edge Case 2
    empty_list = []
    insert_at(empty_list, 0, "Backup SSPA")
    print("After inserting into an empty list:", empty_list)

    # Edge Case 3: Search an empty list.
    result = search_value([], "LNA")
    print("Searching for LNA in an empty list:", result)


if __name__ == "__main__":
    main()