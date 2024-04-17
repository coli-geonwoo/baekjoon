n= int(input())
data= [list(map(int, input().split())) for _ in range(n)]


# 0-가로 1-세로 2-대각선
dp = [[[0]*n for _ in range(n)] for _ in range(3)]

#초기 시작위치
dp[0][0][1]=1

#맨 윗줄 채우기
for i in range(n):
  if data[0][i]==1:
    break
  else:
    dp[0][0][i]=1


for i in range(1, n):
  for j in range(2, n):
    if data[i][j]==1:
      continue
    dp[0][i][j] = dp[0][i][j-1]+ dp[2][i][j-1]
    dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
    if data[i-1][j]==0 and data[i][j-1]==0:
      dp[2][i][j]= dp[0][i-1][j-1]+ dp[1][i-1][j-1]+ dp[2][i-1][j-1]

print(dp[0][n-1][n-1]+ dp[1][n-1][n-1] + dp[2][n-1][n-1])
