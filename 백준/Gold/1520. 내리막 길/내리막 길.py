import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

dp = [[-1] * m for _ in range(n)]
data = [list(map(int, input().split())) for _ in range(n)]
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, before):
    if x == n - 1 and y == m - 1:
        return 1

    temp=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m :
            continue

        if before <= data[nx][ny]:
            continue

        if dp[nx][ny] != -1: #이미 온적 있다면 메모되어 있는 경로 반환
            temp+= dp[nx][ny]
            continue

        temp += dfs(nx, ny, data[nx][ny])

    dp[x][y] = temp #x,y 좌표에서 도달 가능한 경로 메모
    return temp

print(dfs(0, 0, data[0][0]))
