from sympy import isprime

primes = []

def init():
    for i in range(2, 1000):
        if isprime(i):
            primes.append(i)
            

def function(n, a, b):
    return n ** 2 + a * n + b


def main():
    init()
    length = 0
    for b in primes:
        for a in range(-1000, 1001):
            n = 0
            while isprime(function(n, a, b)):
                n += 1
            if n > length:
                length = n
                print(n,a,b)
                ans = a * b
    print(ans)


if __name__ == "__main__":
    main()