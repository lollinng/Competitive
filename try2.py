def findBeforeMatrix(after):

    m = len(after[0])
    n = len(after)
    before = [[0 for i in range(m)] for j in range(n)]

    before[0][0] = after[0][0]

    for i in range(n):
        for j in range(m):
            if (i==0 and j==0):
                continue
            elif (i == 0):
                before[i][j] = after[i][j] - after[i][j - 1]
            elif (j == 0):
                before[i][j] = after[i][j] - after[i - 1][j]
            else:
                before[i][j] = after[i][j] + after[i - 1][j - 1] - after[i - 1][j] - after[i][j - 1]
    return before
