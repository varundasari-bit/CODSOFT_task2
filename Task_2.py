

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    return x / y

def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator symbol (\n1.additon(+)\n2.subtraction(-)\n3.multiplication(*)\n4.division(/)\n from here: ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Try again.\n")
                continue

            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid input. Please enter correct values.\n")

        again = input("Do you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
