# Day 2 - Python Basics: Functions
# Codomax Internship - Ashish Kushwaha

# ============================================
# DEFINING FUNCTIONS
# ============================================
print("=== DEFINING FUNCTIONS ===")

# Basic function with no parameters
def greet():
    """Simple greeting function"""
    print("Hello, welcome to Python!")

greet()
greet()  # Can call multiple times

# Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

greet_person("Ashish")
greet_person("Priya")

# Function with multiple parameters
def introduce(name, age, city="Unknown"):
    """Introduce a person with optional city"""
    print(f"Name: {name}, Age: {age}, City: {city}")

introduce("Ashish", 22)
introduce("Rahul", 25, "Delhi")
introduce(city="Mumbai", name="Sneha", age=24)  # Keyword arguments

# ============================================
# RETURN VALUES
# ============================================
print("\n=== RETURN VALUES ===")

def add(a, b):
    """Add two numbers and return result"""
    return a + b

result = add(10, 5)
print(f"10 + 5 = {result}")

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b with error handling"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

print(f"5 * 6 = {multiply(5, 6)}")
print(f"20 / 4 = {divide(20, 4)}")
print(f"10 / 0 = {divide(10, 0)}")

# Multiple return values (returns tuple)
def get_coordinates():
    """Return x, y coordinates"""
    x = 10
    y = 20
    return x, y  # Returns tuple (10, 20)

x, y = get_coordinates()  # Tuple unpacking
print(f"Coordinates: x={x}, y={y}")

# Return multiple values of different types
def get_student_info():
    return "Ashish", 22, ["Python", "Git"], True

name, age, skills, is_active = get_student_info()
print(f"Student: {name}, Age: {age}, Skills: {skills}, Active: {is_active}")

# ============================================
# DEFAULT PARAMETERS
# ============================================
print("\n=== DEFAULT PARAMETERS ===")

def create_profile(username, role="intern", skills=None):
    """Create user profile with defaults"""
    if skills is None:
        skills = []
    return {
        "username": username,
        "role": role,
        "skills": skills
    }

print(create_profile("ashish123"))
print(create_profile("rahul456", "developer"))
print(create_profile("priya789", skills=["Python", "Django"]))

# ⚠️ DANGEROUS: Mutable default arguments
def bad_example(items=[]):
    items.append("new")
    return items

print(f"\nDangerous mutable default:")
print(f"  First call: {bad_example()}")
print(f"  Second call: {bad_example()}")  # Keeps growing!

# ✅ SAFE: Use None as default
def good_example(items=None):
    if items is None:
        items = []
    items.append("new")
    return items

print(f"\nSafe pattern:")
print(f"  First call: {good_example()}")
print(f"  Second call: {good_example()}")

# ============================================
# *ARGS AND **KWARGS
# ============================================
print("\n=== *ARGS AND **KWARGS ===")

def sum_all(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40): {sum_all(10, 20, 30, 40)}")
print(f"sum_all(*[1,2,3,4]): {sum_all(*[1, 2, 3, 4])}")

def print_info(**kwargs):
    """Print any keyword arguments"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Ashish", age=22, city="Delhi", skill="Python")

def flexible_func(*args, **kwargs):
    """Accept both positional and keyword args"""
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_func(1, 2, 3, name="Ashish", role="Intern")

# ============================================
# LAMBDA FUNCTIONS (Anonymous functions)
# ============================================
print("\n=== LAMBDA FUNCTIONS ===")

# Simple lambda
square = lambda x: x ** 2
print(f"square(5): {square(5)}")

# Lambda with multiple args
add = lambda a, b: a + b
print(f"add(10, 20): {add(10, 20)}")

# Lambda with conditional
max_val = lambda a, b: a if a > b else b
print(f"max(15, 25): {max_val(15, 25)}")

# Using lambda with map, filter, sorted
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# Sort by custom key
students = [
    {"name": "Ashish", "age": 22},
    {"name": "Priya", "age": 20},
    {"name": "Rahul", "age": 25}
]
sorted_by_age = sorted(students, key=lambda s: s["age"])
print(f"Sorted by age: {sorted_by_age}")

# ============================================
# RECURSIVE FUNCTIONS
# ============================================
print("\n=== RECURSIVE FUNCTIONS ===")

def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5): {factorial(5)}")
print(f"factorial(0): {factorial(0)}")

def fibonacci(n):
    """Nth Fibonacci number (recursive)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci sequence (first 10):")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}", end=" ")
print()

# ⚠️ Recursion limit
import sys
print(f"\nRecursion limit: {sys.getrecursionlimit()}")

# ============================================
# DOCSTRINGS AND ANNOTATIONS
# ============================================
print("\n=== DOCSTRINGS & TYPE HINTS ===")

def calculate_area(length: float, width: float) -> float:
    """
    Calculate rectangle area.
    
    Args:
        length: Rectangle length
        width: Rectangle width
    
    Returns:
        Area of rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    return length * width

print(f"Area (5, 3): {calculate_area(5, 3)}")
print(f"Docstring: {calculate_area.__doc__}")
print(f"Annotations: {calculate_area.__annotations__}")

# ============================================
# SCOPE (LEGB Rule)
# ============================================
print("\n=== VARIABLE SCOPE (LEGB) ===")

# L - Local, E - Enclosing, G - Global, B - Built-in

global_var = "I'm global"

def outer():
    enclosing_var = "I'm enclosing"
    
    def inner():
        local_var = "I'm local"
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_var}")
        # print(built_in_var)  # Would error if not defined
    
    inner()

outer()

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(f"\nGlobal counter: {increment()}")
print(f"Global counter: {increment()}")
print(f"Global counter: {increment()}")

# nonlocal for enclosing scope
def outer_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter_fn = outer_counter()
print(f"\nNonlocal counter: {counter_fn()}")
print(f"Nonlocal counter: {counter_fn()}")
print(f"Nonlocal counter: {counter_fn()}")

# ============================================
# PRACTICAL FUNCTION EXAMPLES
# ============================================
print("\n=== PRACTICAL EXAMPLES ===")

# 1. Calculator function
def calculator(a, operation, b):
    """Simple calculator"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Div by zero",
        '//': lambda x, y: x // y if y != 0 else "Error: Div by zero",
        '%': lambda x, y: x % y if y != 0 else "Error: Div by zero",
        '**': lambda x, y: x ** y,
    }
    if operation in operations:
        return operations[operation](a, b)
    return f"Unknown operation: {operation}"

print(f"Calculator: 10 + 5 = {calculator(10, '+', 5)}")
print(f"Calculator: 10 / 3 = {calculator(10, '/', 3)}")
print(f"Calculator: 2 ** 10 = {calculator(2, '**', 10)}")

# 2. Password validator
def validate_password(password):
    """Check password strength"""
    checks = {
        "length": len(password) >= 8,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special": any(not c.isalnum() for c in password)
    }
    score = sum(checks.values())
    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return {
        "checks": checks,
        "score": f"{score}/5",
        "strength": strength[score]
    }

test_passwords = ["123", "password", "Password1", "Pass123!", "Str0ng@Pass#2024"]
for pwd in test_passwords:
    result = validate_password(pwd)
    print(f"Password: '{pwd}' -> {result['strength']} ({result['score']})")

# 3. Text analyzer
def analyze_text(text):
    """Analyze text statistics"""
    words = text.split()
    sentences = text.count('.') + text.count('!') + text.count('?')
    chars = len(text)
    chars_no_spaces = len(text.replace(' ', ''))
    
    return {
        "characters": chars,
        "characters_no_spaces": chars_no_spaces,
        "words": len(words),
        "sentences": sentences,
        "avg_word_length": chars_no_spaces / len(words) if words else 0
    }

sample = "Hello world! This is Python. It's amazing."
analysis = analyze_text(sample)
print(f"\nText analysis: {analysis}")

print("\n✅ Day 2 - Functions Complete!")