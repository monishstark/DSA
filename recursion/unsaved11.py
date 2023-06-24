def shortestDistance(self, N, M, A, X, Y):
    if A[0][0] == 0:
        return -1
    dist = [[float("inf") for i in range(len(A[0]))] for i in range(len(A))]
    dist[0][0] = 0
    q = [[0, 0]]
    while q:
        cur = q.pop(0)
        x, y = cur
        for i, j in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
            if 0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == 1:
                if dist[i][j] > dist[x][y] + 1:
                    dist[i][j] = dist[x][y] + 1
                    q.append([i, j])
    if dist[X][Y] == float("inf"):
        return -1
    return dist[X][Y]
