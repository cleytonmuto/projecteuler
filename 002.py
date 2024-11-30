def main():
    first = 1
    second = 1
    third = first + second
    total = 0
    while third < 4000000:
        third = first + second
        if third % 2 == 0:
            total += third
        first = second
        second = third
    print(total)

if __name__ == "__main__":
    main()