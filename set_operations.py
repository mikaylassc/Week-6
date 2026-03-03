"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 6 Assignment 3
"""
# Create a set with intentional duplicate values
def build_set():
    values = {10, 15, 15, 20, 25}  # Duplicate 15 included on purpose
    print("Original set:", values)
    # Sets automatically remove duplicate values
    return values


# Add and remove elements from the set
def update_set(values):
    values.add(30)     # Add a new number
    values.remove(20)  # Remove an existing number
    print("Modified set:", values)
    return values


# Check if a specific number exists in the set
def check_membership(values):
    exists = 15 in values  # Membership test
    print("Is 15 present in the set?", exists)


# Organize program execution
def main():
    values = build_set()
    values = update_set(values)
    check_membership(values)


# Run the program
if __name__ == "__main__":
    main()