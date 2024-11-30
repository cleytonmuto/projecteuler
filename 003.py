import time # to get execution time
from math import sqrt

def is_prime(n) -> bool:
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return n == 2 or n == 3 or n == 5
    maxP = int(sqrt(n)) + 1
    for d in range(5, maxP):
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True

def main():
    start_time = time.time()
    bigNumber = 600851475143
    ceil = int(sqrt(bigNumber)) + 1
    primes = []
    biggestPrime = 2
    for n in range(ceil):
        if is_prime(n):
            primes.append(n)
    for d in primes:
        if bigNumber % d == 0 and d > biggestPrime:
            biggestPrime = d
            dividend = bigNumber / d
            if is_prime(dividend) and dividend > biggestPrime:
                biggestPrime = dividend
    print(biggestPrime)
    end_time = time.time()
    diff_time = round(end_time - start_time, 3)
    print(f"finished in {diff_time} seconds.")

if __name__ == "__main__":
    main()