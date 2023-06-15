def is_prime(n):
    # Check if n is greater than 2
    if n <= 2:
        return False

    # Check if any number between 2 and n (inclusive) evenly divides n
    for i in range(2, n):
        if n % i == 0:
            return False

    # If no number evenly divides n, it is prime
    return True

n = int(input("Enter a positive integer greater than 2: "))

if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
