"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """
        if node is None:
            return False

        if value == node.value:
            return True

        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)

        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        self._inorder_recursive(node.left, values)

        values.append(node.value)

        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create an empty BST.
    tree = BST()

    # Insert employee/equipment ID numbers.
    values = [1050, 1025, 1075, 1010, 1035, 1060, 1090]

    for value in values:
        tree.insert(value)

    print("Values inserted:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = tree.inorder()

    print("In-order traversal:", traversal)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Values that exist in the tree.
    print("Search for 1035:", tree.search(1035))
    print("Search for 1075:", tree.search(1075))

    # Values that do not exist in the tree.
    print("Search for 1000:", tree.search(1000))
    print("Search for 1100:", tree.search(1100))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Test searching an empty tree.
    empty_tree = BST()

    print("Search empty tree for 1000:",
          empty_tree.search(1000))

    # Test traversing an empty tree.
    print("Empty tree traversal:",
          empty_tree.inorder())

    # Test inserting a duplicate.
    tree.insert(1050)

    print("Traversal after inserting duplicate 1050:",
          tree.inorder())

    # A ground station could organize equipment using numeric equipment IDs.
    # A BST could help locate an equipment ID without checking
    print("\n=== REAL-WORLD BST EXAMPLE ===")

    print("Example: Satellite Ground Station Equipment IDs")

    equipment_tree = BST()

    equipment_ids = [500, 300, 700, 200, 400, 600, 800]

    for equipment_id in equipment_ids:
        equipment_tree.insert(equipment_id)

    print("Equipment IDs:", equipment_ids)

    print("Sorted equipment IDs:",
          equipment_tree.inorder())

    print("Looking for equipment ID 600:",
          equipment_tree.search(600))

    print("Looking for equipment ID 450:",
          equipment_tree.search(450))

if __name__ == "__main__":
    main()