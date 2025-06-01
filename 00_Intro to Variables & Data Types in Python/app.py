"""
Mini Project: Variable Declaration and Type Checking in Python

This program demonstrates how to:
- Declare variables of different data types
- Use the type() function to check variable types
- Print variables with descriptive messages
"""

# Storing user's name (string)
name = "waheed"

# Storing user's age (integer)
age = 22

# Storing voting eligibility status (boolean)
can_vote = True

# Storing a message string with escaped quotes
message = "\"Python is awesome!\""

# Checking and printing the data type of 'name'
print(type(name))  # Output: <class 'str'>

# Checking and printing the data type of 'age'
print(type(age))  # Output: <class 'int'>

# Checking and printing the data type of 'can_vote'
print(type(can_vote))  # Output: <class 'bool'>

# Checking and printing the data type of 'message'
print(type(message))  # Output: <class 'str'>

# Printing a greeting with the name
print("Hello, my name is", name)

# Printing the user's age
print("I am", age, "years old.")

# Printing voting eligibility
print("Am I eligible to vote?", can_vote)

# Printing the custom message
print("My message:", message)
