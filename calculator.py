#define functions for the basic arithematic operaions
def add(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiply(a,b):
    return a * b
 
def divide(a,b):
    if b == 0:
        return "error: division by zero!"
    return a / b

def modulus(a,b):
    if b == 0:
        return "error: modulus by zero"
    return a % b

def exponentiation(a,b):
    if b == 0:
        return 1
    return a ** b
 
#define calculator options
def calculaor():
    print("simple calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. modulus")
    print("6. exponentiation")

while True:
    choice = input("Enter your choice(1/2/3/4/5/6):")
    if choice in['1','2','3','4','5','6']:
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}") 
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '6':
                print(f"{num1} ** {num2} = {exponentiation(num1, num2)}")

        except ValueError:
            print("Invalid input. Please enter a number!")
    else:
        print("Invalid choice. Please enter a valid option!")
        break 

calculator()
            