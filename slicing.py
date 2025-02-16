'''
Slicing in Python

Slicing is a technique in Python used to extract specific parts of lists, tuples, strings,
and other iterable objects using the start:stop:step syntax.

sequence[start:stop:step]
'''


# list
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[1:5])  # Output: [20, 30, 40, 50]
print(numbers[:4])   # Output: [10, 20, 30, 40]  (Start from index 0)
print(numbers[2:])   # Output: [30, 40, 50, 60, 70, 80] (Till end)
print(numbers[-3:])  # Output: [60, 70, 80]  (Negative index slicing)


# String
text = "PythonProgramming"

print(text[0:6])    # Output: Python
print(text[-11:])   # Output: Programming
print(text[::-1])   # Output: gnimmargorPnohtyP (Reverse String)

# Tuple

my_tuple = (1, 2, 3, 4, 5, 6, 7)

print(my_tuple[2:5])  # Output: (3, 4, 5)
print(my_tuple[::2])  # Output: (1, 3, 5, 7) (Every 2nd element)


# Slicing with step in python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])   # Output: [1, 3, 5, 7, 9] (Every 2nd element)
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1] (Reverse list)
