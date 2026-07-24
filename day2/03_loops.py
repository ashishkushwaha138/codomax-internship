# Day 2 - Python Basics: Loops (for, while)
# Codomax Internship - Ashish Kushwaha

# ============================================
# FOR LOOPS
# ============================================
print("=== FOR LOOPS ===")

# Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]
print("Iterating over list:")
for fruit in fruits:
    print(f"  Fruit: {fruit}")

# Iterating over a string
print("\nIterating over string 'PYTHON':")
for char in "PYTHON":
    print(f"  Character: {char}")

# Iterating over range
print("\nUsing range(5):")
for i in range(5):
    print(f"  i = {i}")

print("\nUsing range(2, 8):")
for i in range(2, 8):
    print(f"  i = {i}")

print("\nUsing range(0, 10, 2) - step of 2:")
for i in range(0, 10, 2):
    print(f"  i = {i}")

# Iterating over dictionary
student = {"name": "Ashish", "age": 22, "course": "Python"}
print("\nIterating over dictionary:")
for key in student:
    print(f"  Key: {key}, Value: {student[key]}")

print("\nUsing .items():")
for key, value in student.items():
    print(f"  {key}: {value}")

# Iterating over set
unique_nums = {1, 2, 3, 4, 5}
print("\nIterating over set:")
for num in unique_nums:
    print(f"  Number: {num}")

# enumerate() - get index and value
print("\nUsing enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# zip() - iterate over multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print("\nUsing zip():")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# ============================================
# WHILE LOOPS
# ============================================
print("\n=== WHILE LOOPS ===")

# Basic while loop
count = 1
print("Counting 1 to 5:")
while count <= 5:
    print(f"  Count: {count}")
    count += 1

# While with break
print("\nWhile with break (stop at 3):")
num = 1
while num <= 10:
    if num == 3:
        break
    print(f"  Number: {num}")
    num += 1

# While with continue
print("\nWhile with continue (skip even numbers):")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(f"  Odd number: {num}")

# While-else (else runs when loop completes normally, not broken)
print("\nWhile-else example:")
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    attempts += 1
    print(f"  Attempt {attempts}")
    # Simulate success on 3rd attempt
    if attempts == 3:
        print("  Success!")
        break
else:
    print("  All attempts failed!")

# Infinite loop with break condition
print("\nInfinite loop with break:")
count = 0
while True:
    count += 1
    print(f"  Iteration {count}")
    if count >= 3:
        break

# ============================================
# LOOP CONTROL STATEMENTS
# ============================================
print("\n=== LOOP CONTROL: break, continue, pass ===")

# break - exit loop immediately
print("break example (stop at 5):")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}")

# continue - skip to next iteration
print("\ncontinue example (skip 5):")
for i in range(10):
    if i == 5:
        continue
    print(f"  {i}")

# pass - placeholder (does nothing)
print("\npass example:")
for i in range(3):
    if i == 1:
        pass  # Placeholder for future code
    print(f"  {i}")

# ============================================
# NESTED LOOPS
# ============================================
print("\n=== NESTED LOOPS ===")

# Multiplication table
print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()  # New line after each row

# Pattern printing
print("\nStar pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Nested loop with list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix traversal:")
for row in matrix:
    for element in row:
        print(f"{element}", end=" ")
    print()

# ============================================
# LIST COMPREHENSIONS (Pythonic loops)
# ============================================
print("\n=== LIST COMPREHENSIONS ===")

# Basic list comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(f"Even/Odd labels: {labels}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
print(f"Square dict: {square_dict}")

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "cherry", "date"]}
print(f"Unique word lengths: {unique_lengths}")

# ============================================
# PRACTICAL EXAMPLES
# ============================================
print("\n=== PRACTICAL EXAMPLES ===")

# 1. Sum of numbers 1 to 100
total = sum(range(1, 101))
print(f"Sum 1 to 100: {total}")

# Using loop
total_loop = 0
for i in range(1, 101):
    total_loop += i
print(f"Sum via loop: {total_loop}")

# 2. Find prime numbers up to 50
print("\nPrime numbers up to 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"  {num}", end=" ")
print()

# 3. Fibonacci sequence
print("\nFibonacci (first 10):")
a, b = 0, 1
for _ in range(10):
    print(f"  {a}", end=" ")
    a, b = b, a + b
print()

# 4. Factorial
print("\nFactorial of 5:")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"  5! = {factorial}")

# 5. Guessing game (simulated)
print("\nSimulated number guessing:")
import random
secret = random.randint(1, 20)
guesses = 0
max_guesses = 5

# Simulate guesses
for guess in [10, 15, 12, 14, 13]:
    guesses += 1
    if guess == secret:
        print(f"  Guess {guesses}: {guess} - Correct! The number was {secret}")
        break
    elif guess < secret:
        print(f"  Guess {guesses}: {guess} - Too low!")
    else:
        print(f"  Guess {guesses}: {guess} - Too high!")
else:
    print(f"  Game over! The number was {secret}")

print("\n✅ Day 2 - Loops Complete!")