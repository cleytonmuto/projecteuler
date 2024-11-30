import time # to get execution time

def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def main():
    start_time = time.time()
    N = 1000000
    terms = [0] * N
    map = {} # associates x to f(x), to not re-calculate f(x)
    for n in range(1, N):
        calls = 1
        value = n
        while value != 1:
            calls += 1
            if map.get(value) == None:
                map[value] = collatz(value)
            value = map.get(value)
        terms[n] = calls
    greatestTerm = -1
    bestIndex = 0
    for n in range(N):
        if terms[n] > greatestTerm:
            greatestTerm = terms[n]
            bestIndex = n
    print(f"terms[{bestIndex}] = {terms[bestIndex]} calls")
    end_time = time.time()
    diff_time = round(end_time - start_time, 3)
    print(f"finished in {diff_time} seconds.")

if __name__ == "__main__":
    main()