# Day 2 - Python Basics: Operators
# Codomax Internship - Ashish Kushwaha

# ============================================
# ARITHMETIC OPERATORS
# ============================================
print("=== ARITHMETIC OPERATORS ===")
a, b = 15, 4

print(f"a = {a}, b = {b}")
print(f"Addition (+): {a} + {b} = {a + b}")
print(f"Subtraction (-): {a} - {b} = {a - b}")
print(f"Multiplication (*): {a} * {b} = {a * b}")
print(f"Division (/): {a} / {b} = {a / b}")        # Always returns float
print(f"Floor Division (//): {a} // {b} = {a // b}")  # Integer division
print(f"Modulus (%): {a} % {b} = {a % b}")          # Remainder
print(f"Exponentiation (**): {a} ** {b} = {a ** b}")  # Power

# ============================================
# ASSIGNMENT OPERATORS
# ============================================
print("\n=== ASSIGNMENT OPERATORS ===")
x = 10
print(f"Initial x = {x}")

x += 5   # x = x + 5
print(f"x += 5  -> x = {x}")

x -= 3   # x = x - 3
print(f"x -= 3  -> x = {x}")

x *= 2   # x = x * 2
print(f"x *= 2  -> x = {x}")

x /= 4   # x = x / 4
print(f"x /= 4  -> x = {x}")

x //= 2  # x = x // 2
print(f"x //= 2 -> x = {x}")

x %= 3   # x = x % 3
print(f"x %= 3  -> x = {x}")

x **= 2  # x = x ** 2
print(f"x **= 2 -> x = {x}")

# ============================================
# COMPARISON OPERATORS (Return boolean)
# ============================================
print("\n=== COMPARISON OPERATORS ===")
p, q = 10, 20
print(f"p = {p}, q = {q}")
print(f"Equal (==): {p} == {q} -> {p == q}")
print(f"Not Equal (!=): {p} != {q} -> {p != q}")
print(f"Greater (>): {p} > {q} -> {p > q}")
print(f"Less (<): {p} < {q} -> {p < q}")
print(f"Greater Equal (>=): {p} >= {q} -> {p >= q}")
print(f"Less Equal (<=): {p} <= {q} -> {p <= q}")

# ============================================
# LOGICAL OPERATORS
# ============================================
print("\n=== LOGICAL OPERATORS ===")
x, y = True, False
print(f"x = {x}, y = {y}")
print(f"and: {x} and {y} -> {x and y}")
print(f"or: {x} or {y} -> {x or y}")
print(f"not x: not {x} -> {not x}")
print(f"not y: not {y} -> {not y}")

# Short-circuit evaluation
print("\nShort-circuit examples:")
print(f"True or (1/0): {True or (1/0)}")  # Doesn't evaluate 1/0
print(f"False and (1/0): {False and (1/0)}")  # Doesn't evaluate 1/0

# Practical logical examples
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"\nAge: {age}, Has License: {has_license}")
print(f"Can drive: {can_drive}")

# ============================================
# BITWISE OPERATORS
# ============================================
print("\n=== BITWISE OPERATORS ===")
a, b = 10, 4  # 10 = 1010, 4 = 0100
print(f"a = {a} (binary: {bin(a)}), b = {b} (binary: {bin(b)})")
print(f"AND (&): {a} & {b} = {a & b} (binary: {bin(a & b)})")
print(f"OR (|): {a} | {b} = {a | b} (binary: {bin(a | b)})")
print(f"XOR (^): {a} ^ {b} = {a ^ b} (binary: {bin(a ^ b)})")
print(f"NOT (~): ~{a} = {~a} (binary: {bin(~a)})")
print(f"Left Shift (<<): {a} << 1 = {a << 1} (binary: {bin(a << 1)})")
print(f"Right Shift (>>): {a} >> 1 = {a >> 1} (binary: {bin(a >> 1)})")

# ============================================
# MEMBERSHIP OPERATORS
# ============================================
print("\n=== MEMBERSHIP OPERATORS ===")
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'apple' not in fruits: {'apple' not in fruits}")
print(f"'mango' not in fruits: {'mango' not in fruits}")

# Works with strings, tuples, sets, dicts
text = "hello"
print(f"\nString: '{text}'")
print(f"'e' in text: {'e' in text}")
print(f"'z' in text: {'z' in text}")

# Dictionary checks keys by default
student = {"name": "Ashish", "age": 22}
print(f"\nDict: {student}")
print(f"'name' in student: {'name' in student}")
print(f"'grade' in student: {'grade' in student}")

# ============================================
# IDENTITY OPERATORS
# ============================================
print("\n=== IDENTITY OPERATORS ===")
x = [1, 2, 3]
y = [1, 2, 3]
z = x  # Same reference

print(f"x = {x}, y = {y}, z = x")
print(f"x is y: {x is y}")      # False - different objects
print(f"x == y: {x == y}")      # True - same content
print(f"x is z: {x is z}")      # True - same object
print(f"x is not y: {x is not y}")

# Small integers are cached (-5 to 256)
a = 100
b = 100
print(f"\nSmall int caching: a=100, b=100 -> a is b: {a is b}")
c = 300
d = 300
print(f"Large int: c=300, d=300 -> c is d: {c is d}")

# ============================================
# OPERATOR PRECEDENCE (Highest to Lowest)
# ============================================
print("\n=== OPERATOR PRECEDENCE ===")
# 1. ** (Exponentiation)
# 2. ~ + - (Unary)
# 3. * / // % (Multiplicative)
# 4. + - (Additive)
# 5. << >> (Shifts)
# 6. & (Bitwise AND)
# 7. ^ (Bitwise XOR)
# 8. | (Bitwise OR)
# 9. Comparison (==, !=, >, <, >=, <=, is, is not, in, not in)
# 10. not (Logical NOT)
# 11. and (Logical AND)
# 12. or (Logical OR)
# 13. Assignment (=, +=, -=, etc.)

result = 10 + 5 * 2  # 5*2=10, then 10+10=20
print(f"10 + 5 * 2 = {result}")  # 20, not 30

result = (10 + 5) * 2  # Parentheses first
print(f"(10 + 5) * 2 = {result}")  # 30

# Walrus operator (:=) - Python 3.8+
print("\n=== WALRUS OPERATOR (:=) ===")
# Assign and return value in expression
if (n := len("hello")) > 3:
    print(f"Length {n} > 3")

# In while loop
# while (line := input()) != "quit":
#     print(f"You entered: {line}")

print("\n✅ Day 2 - Operators Complete!")