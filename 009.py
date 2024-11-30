from math import floor, ceil, sqrt

def isPerfectSquare(n) -> bool:
    if floor(sqrt(n)) == ceil(sqrt(n)):
        return True
    return False

def main():
    for a in range(1,1000):
        for b in range(a + 1, 1001):
            c2 = a ** 2 + b ** 2
            if isPerfectSquare(c2):
                c = int(sqrt(c2))
                if a + b + c == 1000:
                    print(a, b, c)
                    print(a * b * c)

if __name__ == "__main__":
    main()