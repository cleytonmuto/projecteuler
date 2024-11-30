from math import sqrt

def divisors_sum(n):
    array = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            array.append(i)
            if i != n // i and i != 1:
                array.append(n // i)
    return sum(array)

def main():
    conjunto = set()
    for n in range(1, 10000):
        d = divisors_sum(n)
        if n == divisors_sum(d) and n != d:
            conjunto.add(n)
            conjunto.add(d)
    print(sum(conjunto))

if __name__ == "__main__":
    main()