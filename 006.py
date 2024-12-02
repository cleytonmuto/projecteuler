def sum_of_squares(n):
    sum = 0
    for k in range(n + 1):
        sum = sum + k ** 2
    return sum

def square_of_sum(n):
    sum = n * (n + 1) / 2
    return sum ** 2

def main():
    print(int(square_of_sum(100) - sum_of_squares(100)))

if __name__ == "__main__":
    main()