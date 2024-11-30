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
    n = 3
    count = 2
    while count < 10001:
        n += 2
        if is_prime(n):
            count += 1
    print(n)

if __name__ == "__main__":
    main()