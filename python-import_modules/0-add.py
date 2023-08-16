# main_program.py

# Define the add function as a placeholder
def add(a, b):
    pass

# Assign values to variables a and b
a = 1
b = 2

# Import the add function from add_0.py
exec(open('add_0.py').read())

# Calculate the result of the addition using the imported add function
result = add(a, b)

# Print the formatted output
print("{} + {} = {}".format(a,b,result))





