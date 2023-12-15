"""Python Built in Functions"""
### abs()	Returns the absolute value of a number
# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true
### ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
### bin()	Returns the binary version of a number
### bytearray()	Returns an array of bytes
### bytes()	Returns a bytes object
### callable()	Returns True if the specified object is callable, otherwise False
### chr()	Returns a character from the specified Unicode code.
# classmethod()	Converts a method into a class method
### compile()	Returns the specified source as an object, ready to be executed
### complex()	Returns a complex number
### delattr()	Deletes the specified attribute (property or method) from the specified object
# dict()	Returns a dictionary (Array)
same_dict = dict(a="b")

# dir()	Returns a list of the specified object's properties and methods
# print(dir(list()))
### divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
### enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
### eval()	Evaluates and executes an expression
### exec()	Executes the specified code (or object)
### filter()	Use a filter function to exclude items in an iterable object
# float()	Returns a floating point number
### format()	Formats a specified value
### frozenset()	Returns a frozenset object
# getattr()	Returns the value of the specified attribute (property or method)
### globals()	Returns the current global symbol table as a dictionary
# hasattr()	Returns True if the specified object has the specified attribute (property/method)
# hasattr(same_dict, "pop")
### hash()	Returns the hash value of a specified object
### help()	Executes the built-in help system
### hex()	Converts a number into a hexadecimal value
# id()	Returns the id of an object
# input()	Allowing user input
# int()	Returns an integer number
# isinstance()	Returns True if a specified object is an instance of a specified object
# print(isinstance(same_dict, dict))
### issubclass()	Returns True if a specified class is a subclass of a specified object
### iter()	Returns an iterator object
# len()	Returns the length of an object
# list()	Returns a list
# a_list = list((1,"a", 2))
# print(a_list)
### locals()	Returns an updated dictionary of the current local symbol table
# map()	Returns the specified iterator with the specified function applied to each item
words = ['apple', 'banana', 'cherry']
nums = ["1", 2.5, "3"]
upper_words = list(map(int, nums))
# print(upper_words)
# max()	Returns the largest item in an iterable
spisok = [3, 4, 100, 1, 5]
# print(max(spisok))
### memoryview()	Returns a memory view object
# min()	Returns the smallest item in an iterable
# print("min(spisok)", min(spisok))
# next()	Returns the next item in an iterable
### object()	Returns a new object
### oct()	Converts a number into an octal
### open()	Opens a file and returns a file object
### ord()	Convert an integer representing the Unicode of the specified character
# pow()	Returns the value of x to the power of y
# print()	Prints to the standard output device

### property()	Gets, sets, deletes a property
# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
values = (0, 1, 2, 3, 9)
#range(1000000)
# print("*"*88)
# for i in range(5, 20, 3):
#     print(i)
### repr()	Returns a readable version of an object
### reversed()	Returns a reversed iterator
### round()	Rounds a numbers
# set()	Returns a new set object
### setattr()	Sets an attribute (property/method) of an object
### slice()	Returns a slice object
# sorted()	Returns a sorted list
# print("a", spisok)
# print("b", sorted(spisok))
# print("c", spisok.sort())

# staticmethod()	Converts a method into a static method
# str()	Returns a string object
# sum()	Sums the items of an iterator
# print(sum((1,3,2,4)))
# super()	Returns an object that represents the parent class
# tuple()	Returns a tuple
# type()	Returns the type of an object
# print(type(1))
### vars()	Returns the __dict__ property of an object
# zip()	Returns an iterator, from two or more iterators
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# print(dict(zip(list2, list1)))

print("*"*88)
# Додавання нової функції - Adding new functions
# def print_lyrics():
#     """Друкує пісню"""
#     print("Ой у лузі червона калина похилилася")
#     print("Чогось наша славна Україна зажурилася")

# print_lyrics()

# Виклик функції
# Параметри та аргументи - Parameters and arguments
# def square(number:int) -> int:
#     """Calculate the square of number."""
#     return number ** 2

# print("3**2:", square(3))
# print("2**2:", square(2))

# Функція з аргументами
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     return f"My {animal_type}'s name is {pet_name.title()}."
# print(describe_pet("shinshila", "pyizhyk"))
# print(describe_pet("pyizhyk", "shinshila"))

# def make_pizza(*toppings):


# def comma(*args) -> int:
#     return ",".join([str(a) for a in args])
# print(comma(1))
# print(comma(1, 2))
# print(comma(1, 2, 3))

# def make_pizza(*toppings):
#     return f"your pizza contains: {', '.join(toppings)}"

# print(make_pizza("aplle", "banana", "kivi"))

# print(comma(1, 2, 3))

# Опційні задані значення аргументів - Making an Argument Optional
# def spam(a, b=42):
#     return (a + b)
# print(spam(1))
# print(spam(1, 1))

# def spam_two(a, b, c=3, d=42):
#     return (a + b)

# def spam_third(a, *args):
#     return (a)
# print(spam_third(1, 2, 3, 5, "ffff"))

# def kward_spam(**kwargs):
#     return (kwargs["a"]+kwargs["b"])

# print(kward_spam(a=1, b=2))