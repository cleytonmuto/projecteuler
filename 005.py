def gcd(a,b):
    return a if b == 0 else gcd(b,a % b)

def lcm(a,b):
    return int(a * b / gcd(a,b))

def main():
    common = 1
    for m in range(1,21):
        common = lcm(common,m)
    print(common)

if __name__ == "__main__":
    main()