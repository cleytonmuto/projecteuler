import time # to get execution time
from math import sqrt

def is_prime(n) -> bool:
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return n == 2 or n == 3 or n == 5
    maxP = int(sqrt(n)) + 1
    for d in range(5, maxP, 6):
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True

def main():
    start_time = time.time()
    sum = 5
    for n in range(5, 2000000, 6):
        if is_prime(n):
            sum += n
        if is_prime(n + 2):
            sum += n + 2
    print(sum)
    end_time = time.time()
    diff_time = round(end_time - start_time, 3)
    print(f"finished in {diff_time} seconds.")

if __name__ == "__main__":
    main()