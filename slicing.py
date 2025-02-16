'''
Slicing in Python

Slicing is a technique in Python used to extract specific parts of lists, tuples, strings,
and other iterable objects using the start:stop:step syntax.

sequence[start:stop:step]
'''

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[1:5])  # Output: [20, 30, 40, 50]
print(numbers[:4])   # Output: [10, 20, 30, 40]  (Start from index 0)
print(numbers[2:])   # Output: [30, 40, 50, 60, 70, 80] (Till end)
print(numbers[-3:])  # Output: [60, 70, 80]  (Negative index slicing)
