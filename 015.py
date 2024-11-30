def main():
    N = 21
    matrix = matrix = [ [ 0 for i in range(N) ] for j in range(N) ]
    for k in range(N):
        matrix[0][k] = 1
        matrix[k][0] = 1
    for i in range(1,N):
        for j in range(1,N):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    print(matrix[N - 1][ N - 1])

if __name__ == "__main__":
    main()