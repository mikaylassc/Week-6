"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 6 Assignment 2
"""
# This function creates and prints a tuple of three cities
def create_tuple():
    cities = ("Seattle", "Atlanta", "Denver")  # Parentheses create a tuple
    print("Cities:", cities)
    return cities


# This function accesses and prints the second city
def access_tuple(cities):
    print("Second city:", cities[1])  # Index 1 = second element


# This function attempts to modify the tuple (this will cause an error)
def modify_tuple(cities):
    # This line raises: TypeError: 'tuple' object does not support item assignment.
    # The error occurs because tuples are immutable, meaning once created, their elements cannot be changed, replaced, or reassigned.
    cities[1] = "Boston"


# Main function to control program flow
def main():
    cities = create_tuple()
    access_tuple(cities)
    modify_tuple(cities)  # Program intentionally stops here


# Runs the program
if __name__ == "__main__":
    main()