def main():
    sumOfTheSquares = 0
    squareOfTheSum = 0
    for n in range(101):
        sumOfTheSquares += n ** 2
        squareOfTheSum += n
    squareOfTheSum = squareOfTheSum ** 2
    print(squareOfTheSum - sumOfTheSquares)

if __name__ == "__main__":
    main()