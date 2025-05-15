# Python Basics Practice

# 1. Data Types Practice
print("=== Data Types ===")
my_int = 42
my_float = 3.14
my_str = "Hello, World!"
my_bool = True
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "Alice", "age": 25, "city": "NYC"}

print(f"Integer: {my_int}, Type: {type(my_int)}")
print(f"Float: {my_float}, Type: {type(my_float)}")
print(f"String: {my_str}, Type: {type(my_str)}")

# 2. Control Flow Practice
print("\n=== Control Flow ===")
# If statements
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Score: {score}, Grade: {grade}")

# For loops
print("\nFor loop examples:")
for i in range(5):
    print(f"Iteration {i}")

# While loops
print("\nWhile loop example:")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1

# Break and continue
print("\nBreak and continue:")
for i in range(10):
    if i == 2:
        continue  # Skip 2
    if i == 5:
        break  # Stop at 5
    print(i)

# 3. Functions Practice
print("\n=== Functions ===")
def greet(name, greeting="Hello"):
    """Simple greeting function with default argument"""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# *args and **kwargs
def flexible_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=25)

# 4. Comprehensions Practice
print("\n=== Comprehensions ===")
# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# Dict comprehension
char_counts = {char: ord(char) for char in "ABC"}
print(f"Character codes: {char_counts}")

# Set comprehension
unique_evens = {x for x in [1, 2, 2, 3, 4, 4, 5] if x % 2 == 0}
print(f"Unique evens: {unique_evens}")

# 5. Common Built-ins Practice
print("\n=== Common Built-ins ===")
numbers = [3, 1, 4, 1, 5, 9]

print(f"Length: {len(numbers)}")
print(f"Range 1-5: {list(range(1, 6))}")
print(f"Zip example: {list(zip([1, 2, 3], ['a', 'b', 'c']))}")
print(f"Enumerate: {list(enumerate(['apple', 'banana', 'cherry']))}")
print(f"Map (square): {list(map(lambda x: x**2, numbers))}")
print(f"Filter (evens): {list(filter(lambda x: x % 2 == 0, numbers))}")
print(f"Any > 5: {any(x > 5 for x in numbers)}")
print(f"All > 0: {all(x > 0 for x in numbers)}")
print(f"Sorted: {sorted(numbers)}")
print(f"Sorted (reverse): {sorted(numbers, reverse=True)}")

# Practice Problem: Reverse a string using multiple methods
print("\n=== Practice: Reverse String ===")
def reverse_string(s):
    return s[::-1]

def reverse_string_iterative(s):
    return ''.join(reversed(s))

def reverse_string_manual(s):
    result = ""
    for char in s:
        result = char + result
    return result

test_string = "Python"
print(f"Original: {test_string}")
print(f"Method 1 (slice): {reverse_string(test_string)}")
print(f"Method 2 (reversed): {reverse_string_iterative(test_string)}")
print(f"Method 3 (manual): {reverse_string_manual(test_string)}")

# Practice Problem: Check if palindrome
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(f"\nIs 'racecar' a palindrome? {is_palindrome('racecar')}")
print(f"Is 'A man, a plan, a canal: Panama' a palindrome? {is_palindrome('A man, a plan, a canal: Panama')}")