def fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter the value of n: "))
print("The", n, "th Fibonacci number is", fibonacci(n))