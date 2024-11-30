def main():
    map = {}
    map[0] = 123
    map[1] = 456
    map[2] = 789
    for i in range(4):
        if map.get(i) == None:
            map[i] = 999
        print(map.get(i))

if __name__ == "__main__":
    main()