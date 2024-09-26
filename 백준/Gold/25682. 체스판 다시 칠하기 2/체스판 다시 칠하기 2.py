import sys

def answer(solution):
    cur_sum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cur_sum[i][j] = cur_sum[i][j - 1] + cur_sum[i-1][j] - cur_sum[i-1][j-1]
            if solution[i - 1][j - 1] != data[i - 1][j - 1]:
                cur_sum[i][j] += 1

    result = sys.maxsize

    # for i in range(1, n+1):
    #     print(*cur_sum[i][1:])
    # print()

    for i in range(k, n + 1):
        for j in range(k, m + 1):
            cnt = cur_sum[i][j] - (cur_sum[i - k][j] + cur_sum[i][j - k]) + cur_sum[i - k][j - k]
            result = min(result, cnt)

    return result


n,m,k= map(int, input().split())
data = [list(input()) for _ in range(n)]
solution1 =[[0]*m for _ in range(n)]
solution2 =[[0]*m for _ in range(n)]

# for i in range(n):
#     print(*data[i])

for i in range(n):
    for j in range(m):
        if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
            solution1[i][j] = "B"
            solution2[i][j] = "W"
        else:
            solution1[i][j] = "W"
            solution2[i][j] = "B"

print(min(answer(solution1), answer(solution2)))


