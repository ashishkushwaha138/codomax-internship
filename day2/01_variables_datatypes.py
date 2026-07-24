# Day 2 - Python Basics: Variables and Data Types
# Codomax Internship - Ashish Kushwaha

# ============================================
# VARIABLES IN PYTHON
# ============================================
# Variables are containers for storing data values
# Python has no command for declaring a variable
# A variable is created the moment you first assign a value to it

# Variable naming rules:
# - Must start with a letter or underscore
# - Cannot start with a number
# - Can only contain alpha-numeric characters and underscores (A-z, 0-9, _)
# - Case-sensitive (age, Age, AGE are different)

# Examples of valid variable names
name = "Ashish"           # String
age = 22                  # Integer
height = 5.9              # Float
is_student = True         # Boolean
skills = ["Python", "Git", "Linux"]  # List

# Multiple assignment
x = y = z = 100
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# Swapping variables (Pythonic way)
a, b = 10, 20
a, b = b, a
print(f"After swap: a={a}, b={b}")

# ============================================
# DATA TYPES IN PYTHON
# ============================================

# 1. TEXT TYPE: str (String)
text = "Hello, Python!"
multiline = """This is a
multi-line string"""
print(f"\n--- String Examples ---")
print(f"String: {text}")
print(f"Length: {len(text)}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")

# 2. NUMERIC TYPES
# int (Integer) - whole numbers
integer_num = 42
negative_int = -10
print(f"\n--- Numeric Types ---")
print(f"Integer: {integer_num}, Type: {type(integer_num)}")

# float (Floating point) - decimal numbers
float_num = 3.14
scientific = 1e5  # 100000.0
print(f"Float: {float_num}, Scientific: {scientific}")

# complex (Complex numbers)
complex_num = 3 + 4j
print(f"Complex: {complex_num}, Real: {complex_num.real}, Imag: {complex_num.imag}")

# 3. SEQUENCE TYPES
# list - ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Mutable
print(f"\n--- Sequence Types ---")
print(f"List: {fruits}")

# tuple - ordered, immutable, allows duplicates
coordinates = (10, 20)
# coordinates[0] = 5  # This would raise an error!
print(f"Tuple: {coordinates}")

# range - sequence of numbers
numbers = range(5)  # 0, 1, 2, 3, 4
print(f"Range: {list(numbers)}")

# 4. MAPPING TYPE: dict (Dictionary) - key-value pairs, mutable
student = {
    "name": "Ashish",
    "age": 22,
    "course": "Python Internship",
    "skills": ["Python", "Git"]
}
print(f"\n--- Mapping Type ---")
print(f"Dictionary: {student}")
print(f"Name: {student['name']}")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

# 5. SET TYPES
# set - unordered, no duplicates, mutable
unique_numbers = {1, 2, 3, 3, 4}  # Duplicates removed
unique_numbers.add(5)
print(f"\n--- Set Types ---")
print(f"Set: {unique_numbers}")

# frozenset - immutable version of set
frozen = frozenset([1, 2, 3, 4])
print(f"Frozenset: {frozen}")

# 6. BOOLEAN TYPE: bool - True or False
is_true = True
is_false = False
print(f"\n--- Boolean Type ---")
print(f"True: {is_true}, False: {is_false}")
print(f"10 > 5: {10 > 5}")
print(f"bool(0): {bool(0)}, bool(1): {bool(1)}")
print(f"bool(''): {bool('')}, bool('hello'): {bool('hello')}")

# 7. BINARY TYPES
# bytes - immutable sequence of bytes
byte_data = b"hello"
print(f"\n--- Binary Types ---")
print(f"Bytes: {byte_data}")

# bytearray - mutable sequence of bytes
byte_array = bytearray(b"hello")
byte_array[0] = ord('H')
print(f"Bytearray: {byte_array}")

# memoryview - memory view object
mem_view = memoryview(b"hello")
print(f"Memoryview: {mem_view.tobytes()}")

# 8. NONE TYPE
nothing = None
print(f"\n--- None Type ---")
print(f"None: {nothing}, Type: {type(nothing)}")

# ============================================
# TYPE CONVERSION (CASTING)
# ============================================
print(f"\n--- Type Conversion ---")
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print(f"String '{num_str}' -> int: {num_int}, float: {num_float}")

# Convert to string
value = 42
str_value = str(value)
print(f"Int {value} -> String: '{str_value}'")

# Convert to list/tuple/set
text = "hello"
print(f"String to list: {list(text)}")
print(f"String to tuple: {tuple(text)}")
print(f"String to set: {set(text)}")

# ============================================
# CHECKING DATA TYPES
# ============================================
print(f"\n--- Type Checking ---")
variables = [name, age, height, is_student, skills, student, unique_numbers, nothing]
for var in variables:
    print(f"Value: {var} | Type: {type(var).__name__}")

# isinstance() - recommended way to check types
print(f"\nisinstance(age, int): {isinstance(age, int)}")
print(f"isinstance(name, str): {isinstance(name, str)}")

print("\n✅ Day 2 - Variables & Data Types Complete!")