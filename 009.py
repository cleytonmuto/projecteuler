def main():
    for a in range(998):
        for b in range(a + 1, 999):
            for c in range(b + 1, 1000):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    print(a, "*", b, "*", c, "=", a * b * c)
                    return
    

if __name__ == "__main__":
    main()