# 1)	Let, a new implementation of python uses mutable objects as key for dictionary. What are the side effects?

# Create a list
# my_list = [1, 2, 3]
# 
# # Try to use the list as a key in a dictionary
# try:
#     my_dict = {my_list: "Hello"}
# except TypeError as e:
#     print(f"Error: {e}")

# Hypothetical mutable key



mutable_key = MutableObject()

# Create a dictionary with the mutable key
my_dict = {mutable_key: "Hello"}

# Print the value associated with the mutable key
print(my_dict[mutable_key])  # Output: "Hello"

# Modify the mutable key
mutable_key.modify()

# Try to print the value associated with the mutable key
print(my_dict[mutable_key])  # This would raise a KeyError
