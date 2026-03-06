# Calculator Project - Main Branch
# A simple calculator with 5 functions

def addition(a, b):
    """Function 1: Addition"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

def subtraction(a, b):
    """Function 2: Subtraction"""
    result = a - b
    print(f"{a} - {b} = {result}")
    return result

def multiplication(a, b):
    """Function 3: Multiplication"""
    result = a * b
    print(f"{a} * {b} = {result}")
    return result

def division(a, b):
    """Function 4: Division"""
    result = a / b
    print(f"{a} / {b} = {result}")
    return result

def modulus(a, b):
    """Function 5: Modulus"""
    result = a % b
    print(f"{a} % {b} = {result}")
    return result


# Main execution
if __name__ == "__main__":
    print("===== Simple Calculator =====")
    print("Developed on main branch")
    print()
    addition(10, 5)
    subtraction(10, 5)
    multiplication(10, 5)
    division(10, 5)
    modulus(10, 3)