def find_primes(n):
    # Create a list of boolean values indicating whether each number is prime
    primes = [True] * (n + 1)

    # 0 and 1 are not prime, so mark them as False
    primes[0] = primes[1] = False

    # Loop through all numbers from 2 to n (inclusive)
    for i in range(2, n + 1):
        # If i is prime, mark all its multiples as not prime
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Return a list of all prime numbers less than or equal to n
    return [i for i in range(2, n + 1) if primes[i]]

n = int(input("Enter a positive integer greater than 1: "))

primes = find_primes(n)

print("Prime numbers less than or equal to", n, "are:")
print(primes)
