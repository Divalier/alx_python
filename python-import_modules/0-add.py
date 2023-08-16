# 0-add.py

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b

if __name__ == "__main__":
    # Assign values to variables a and b
    a = 1
    b = 2

    # Calculate the result of the addition
    result = add(a, b)

    # Print the formatted output
    print(f"{a} + {b} = {result}")
