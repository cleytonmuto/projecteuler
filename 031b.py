def main():
    total = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    # ways[i] = number of ways to make sum i
    ways = [1] + [0] * total
    for coin in coins:
        for i in range(total - coin + 1):
            ways[i + coin] += ways[i]
    print(ways[total])


if __name__ == "__main__":
    main()
