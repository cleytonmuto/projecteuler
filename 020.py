import math

def main():
    strArray = list(str(math.factorial(100)))
    array = [int(x) for x in strArray]
    print(sum(array))

if __name__ == "__main__":
    main()
