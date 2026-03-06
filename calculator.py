# Calculator Project - Updated by Developer 2
# A simple calculator with 5 functions - Improved Version

def addition(a, b):
    """Function 1: Addition - Updated by Developer2"""
    result = a + b
    print(f"[Developer2] Addition: {a} + {b} = {result}")
    return result

def subtraction(a, b):
    """Function 2: Subtraction - Updated by Developer2"""
    result = a - b
    print(f"[Developer2] Subtraction: {a} - {b} = {result}")
    return result

def multiplication(a, b):
    """Function 3: Multiplication - Updated by Developer2"""
    result = a * b
    print(f"[Developer2] Multiplication: {a} * {b} = {result}")
    return result

def division(a, b):
    """Function 4: Division - improved by Developer2"""
    try:
        result = a / b
        print(f"[Developer2] Division: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("[Developer2] Division by zero is not allowed!")
        return None

def modulus(a, b):
    """Function 5: Modulus - improved by Developer2"""
    try:
        result = a % b
        print(f"[Developer2] Modulus: {a} % {b} = {result}")
        return result
    except ZeroDivisionError:
        print("[Developer2] Modulus by zero is not allowed!")
        return None


# Main execution
if __name__ == "__main__":
    print("===== Simple Calculator =====")
    print("Updated by Developer2 - Added try-except error handling")
    print()
    
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ")
        
        if choice == '6':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                addition(a, b)
            elif choice == '2':
                subtraction(a, b)
            elif choice == '3':
                multiplication(a, b)
            elif choice == '4':
                division(a, b)
            elif choice == '5':
                modulus(a, b)
        else:
            print("Invalid choice! Please select 1-6.")