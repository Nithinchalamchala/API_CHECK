"""Test script with intentional bugs for pipeline validation."""

# 1. Import Error: Importing a non-existent module
import this_module_does_not_exist
import sys
import missing_package

def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b

# 2. Syntax Error: Missing colon and mismatched parentheses
def buggy_function(x, y)
    result = (x + y * 2
    return result

def check_conditions(data):
    if data:
        # Bare except which catches everything
        try:
            print("Data is valid")
        except:
            print("An error occurred")
            
# 3. Infinite Loop: While True without a break
def loop_forever():
    count = 0
    while True:
        count += 1
        # No break condition causes an infinite loop
        # print(f"Looping forever... count: {count}")

if __name__ == "__main__":
    print "Starting the buggy script"  # Syntax error in Python 3, missing parens
    loop_forever()
