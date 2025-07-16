# is identifiers
# format
# newStr : str = 'sampleText'
# newStr.format() // inbuild string method
# format() is a versatile inbuilt method to format 
# strings allowing us to use placeholder values which are denoted inside {}
# f'' [ f Strings ] is short hand of doing it for more cleaner code and formatting.
name = "Alice"
age = 30
city = "New Jersey"

# Basic usage with positional arguments
message1 = "Hello, {}! You are {} years old.".format(name, age)
print(message1)

# Using indexed arguments
message2 = "You are from {1}, {0}.".format(name, city)
print(message2)


# isidentifier() | In python isidentifier is a built-in string method which
# is used to check if a given string is a valid Python Identifier or not.
# it return bool either True or False depends on the following 
# Python Valid Identifier Rules
# Rule 1: an Identifier should start with a letter (a-z,A-Z,) or an underscore (_)
# Rule 2: --||-- should not start with a digit (0-9)
# Rule 3: --||-- cannot contain special characters (@,#,$,%,^,&....etc or `,`, `.`, ...)
# Rule 4: even if the identifier starts with letters it should not be any Python Keyword
# For eg. (for, True, False, while, def, class, etc...)
# Valid identifiers
print("my_variable".isidentifier())  # True
print("_function_name".isidentifier()) # True
print("Class123".isidentifier())     # True
