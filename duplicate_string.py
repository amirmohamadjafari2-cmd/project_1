"""
Assignment: Recursive Functions
Problem: Checking if a string is Duplicate.
"""

def is_duplicate(s: str) -> bool:
    """
    Recursively checks whether a string is Duplicate.
    """

    # Rule (a): Empty strings are Duplicate
    if len(s) == 0:
        return True

    # Rule (b): Check if the length is even
    n = len(s)

    if n % 2 != 0:
        return False

    # Divide the string into two equal halves
    half_len = n // 2
    first_half = s[:half_len]
    second_half = s[half_len:]

    # Both halves must be equal
    if first_half != second_half:
        return False

    # Rule (c): Remove the first character
    # of the first half and check recursively
    remaining_string = first_half[1:]

    return is_duplicate(remaining_string)


# Get input repeatedly until the user exits
while True:
    user_string = input("Enter a string (or type 'exit' to quit): ")

    if user_string.lower() == "exit":
        print("Program finished.")
        break

    result = is_duplicate(user_string)
    print("Duplicate:", result)
    