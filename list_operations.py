"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 6 Assignment 1
"""
# This function creates a list of numbers from 1 to 10
def create_list():
    numbers = list(range(1, 11))  # Generates numbers 1 through 10
    print("Original list:", numbers)
    return numbers


# This function updates the list
def modify_list(numbers):
    numbers.append(11)   # Add 11 to the end
    numbers.remove(5)    # Remove the value 5
    print("Updated list:", numbers)
    return numbers


# This function slices the first five elements
def slice_list(numbers):
    first_five = numbers[:5]  # Get first five elements
    print("First five elements:", first_five)


# Main function to organize program flow
def main():
    numbers = create_list()
    numbers = modify_list(numbers)
    slice_list(numbers)


# Runs the program
if __name__ == "__main__":
    main()