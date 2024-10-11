import sys
from collections import deque


def bfs():
    q = deque([(0, sx, sy)])
    data = [[INF] * n for _ in range(n)]
    data[sx][sy] = 0

    while (q):
        cnt, x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or data[nx][ny] <= cnt + 1:
                continue
            if (nx, ny) == (ex, ey):
                return cnt + 1
            data[nx][ny] = cnt + 1
            q.append((cnt + 1, nx, ny))


for _ in range(int(input())):
    n = int(input())

    dx = [-2, -2, 2, 2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    INF = sys.maxsize
    if (sx, sy) == (ex, ey):
        print(0)
    else:
        print(bfs())
