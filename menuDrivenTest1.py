

def add(a, b):
    sum = a + b
    print(sum)

def subtract(a, b):
    difference = a - b
    print(difference)

def multiply(a, b):
    product = a * b
    print(product)

def divide(a, b):
    quotient = a / b
    print(quotient)


def main():
    print("WELCOME TO CALCULATOR")

    while True:
        print("MENU")
        print("1. Addition of 2 numbers")
        print("2. Difference of 2 numbers")
        print("3. Multiplication of 2 numbers")
        print("4. Division of 2 numbers")
        print("5. Exit")
        userChoice = int(input("\n Enter your choice: "))


        if userChoice == 1:
            print("\n PERFORMING ADDITION\n")
            a = int(input("What us your first number: "))
            b = int(input("What is your second number: "))
            add(a, b)

        elif userChoice == 2:
            print("\n PERFORMING SUBTRACTION\n")
            a = int(input("What us your first number: "))
            b = int(input("What is your second number: "))
            subtract(a, b)

        elif userChoice == 3:
            print("\n PERFORMING MULTIPLICATION\n")
            a = int(input("What us your first number: "))
            b = int(input("What is your second number: "))
            multiply(a, b)

        elif userChoice == 4:
            print("\n PERFORMING DIVISION\n")
            a = int(input("What us your first number: "))
            b = int(input("What is your second number: "))
            divide(a, b)

        elif userChoice == 5:
            break

        else:
            print("Please enter a valid input from the list: ")

if __name__ == '__main__':
    main()