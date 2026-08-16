"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "Parent"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Category: {self.category}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    school = "Generic School"

    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def study(self):
        return f"{self.name} is studying {self.major}."

    def display_info(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"ID: {self.student_id}, Major: {self.major}, "
                f"School: {self.school}")

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass("Alex", 20, "S1001", "Computer Science")
    student2 = ChildClass("Jordan", 21, "S1002", "Cybersecurity")

    print("Class variable through class:", ChildClass.school)
    print("Class variable through student1:", student1.school)

    student1.favorite_color = "Blue"

    print("\nstudent1 namespace:")
    print(student1.__dict__)

    print("\nstudent2 namespace:")
    print(student2.__dict__)

    print("\nChildClass namespace:")
    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass("Taylor", 22, "S1003", "Computer Science")
    original.courses = ["Python", "Networking", ["Database"]]

    shallow_copy = copy(original)

    deep_copy = deepcopy(original)

    original.courses[2].append("SQL")

    print("Original:")
    print(original.__dict__)

    print("\nShallow Copy:")
    print(shallow_copy.__dict__)

    print("\nDeep Copy:")
    print(deep_copy.__dict__)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    parent = ParentClass("Chris", 40)
    print(parent.display_info())

    print("\n=== Child Object ===")
    child = ChildClass("Morgan", 19, "S2001", "Computer Science")

    print(child.display_info())

    print(child.study())

    demonstrate_namespaces()

    demonstrate_copying()


if __name__ == "__main__":
    main()