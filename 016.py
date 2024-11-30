def main():
    strArray = list(str(2 ** 1000))
    array = [int(x) for x in strArray]
    print(sum(array))

if __name__ == "__main__":
    main()