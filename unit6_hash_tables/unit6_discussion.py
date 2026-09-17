"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================

    # Creates an empty dictionary
    tool_inventory = {}


    print("\n=== INSERT OPERATIONS ===")

    # The tool ID is the key and the tool name is the value.
    tool_inventory[101] = "Cordless Drill"
    tool_inventory[102] = "Circular Saw"
    tool_inventory[103] = "Socket Set"
    tool_inventory[104] = "Torque Wrench"
    tool_inventory[105] = "Multimeter"

    # Display the contents of the dictionary
    print("Tool inventory:", tool_inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # Retrieve two existing keys
    print("Tool ID 103:", tool_inventory[103])
    print("Tool ID 105:", tool_inventory[105])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", tool_inventory)

    # Assigning a new value to an existing key replaces the old value.
    # Update the value for Tool ID 104
    tool_inventory[104] = "Digital Torque Wrench"

    print("After update:", tool_inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", tool_inventory)

    # Deleting a key removes the key and its associated value.
    # Delete Tool ID 102.
    del tool_inventory[102]

    print("After deletion:", tool_inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Lookup a missing key.
    missing_tool = tool_inventory.get(999, "Tool not found")
    print("Lookup Tool ID 999:", missing_tool)

    # Edge Case 2: Delete a missing key safely.
    removed_tool = tool_inventory.pop(200, "Tool not found")
    print("Delete Tool ID 200:", removed_tool)

if __name__ == "__main__":
    main()