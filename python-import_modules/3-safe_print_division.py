def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Division by zero is not allowed")
    finally:
        print("Inside result: {}".format(result))
        return result


