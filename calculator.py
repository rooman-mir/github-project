# Calculator Project - Updated by Developer 1
# A simple calculator with 5 functions - Enhanced Version

def addition(a, b):
    """Function 1: Addition - Updated by Developer1"""
    result = a + b
    print(f"[Developer1] {a} + {b} = {result}")
    return result

def subtraction(a, b):
    """Function 2: Subtraction - Updated by Developer1"""
    result = a - b
    print(f"[Developer1] {a} - {b} = {result}")
    return result

def multiplication(a, b):
    """Function 3: Multiplication - Updated by Developer1"""
    result = a * b
    print(f"[Developer1] {a} * {b} = {result}")
    return result

def division(a, b):
    """Function 4: Division - with error handling by Developer1"""
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    result = a / b
    print(f"[Developer1] {a} / {b} = {result}")
    return result

def modulus(a, b):
    """Function 5: Modulus - with error handling by Developer1"""
    if b == 0:
        print("Error: Cannot perform modulus by zero!")
        return None
    result = a % b
    print(f"[Developer1] {a} % {b} = {result}")
    return result


# Main execution
if __name__ == "__main__":
    print("===== Simple Calculator =====")
    print("Updated by Developer1 - Added error handling")
    print()
    addition(10, 5)
    subtraction(10, 5)
    multiplication(10, 5)
    division(10, 0)
    modulus(10, 3)