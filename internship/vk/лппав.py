def knapSack(W, wt, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(val[i - 1]
                                  + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]



if __name__ == "__main__":
    W = [15, 10, 2, 4]
    V = [30, 25, 2, 6]
    W = 61
    n = 14

    wt=[26,9,1,6,8,11,3,9,27,10,19,21,26,23]
    val=[32,13,38,37,16,31,38,20,27,31,11,2,39,9]
    print(knapSack(W, wt, val))