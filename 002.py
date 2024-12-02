def main():
    first, second, third, sum, max = 1, 1, 0, 0, 4000000
    while third < max:
        third = first + second
        if third % 2 == 0 and third < max:
            sum += third
        first = second
        second = third
    print(sum)

if __name__ == "__main__":
    main()