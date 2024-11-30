def main():
    greatest = 1
    for x in range(100,1000):
        for y in range(100,1000):
            product = x * y
            strProduct = str(product)
            if strProduct == strProduct[::-1] and product > greatest:
                greatest = product
    print(greatest)

if __name__ == "__main__":
    main()