# source: https://stackoverflow.com/questions/15347174/python-finding-prime-factors

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def main():
    N = 600851475143
    print(largest_prime_factor(N))
    print(prime_factors(N))

if __name__ == "__main__":
    main()