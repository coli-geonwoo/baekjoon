#20002. 사과나무(골5)
# 좌표평면에서 정사각형 누적합 더하기

import sys

input = lambda: sys.stdin.readline().strip('\n')
#각 정사각형의 넓이
def getSquareBenefit(i,j,k):
  global data
  if i+k>n or j+k>n:
    return

  return data[i+k][j+k]- data[i-1][j+k] - data[i+k][j-1] + data[i-1][j-1]


n= int(input())

data= [[0]*(n+1)]
for _ in range(n):
  data.append([0]+ list(map(int, input().split())))

#각 꼭짓점까지의 누적합 구하기
for i in range(1, n+1):
  for j in range(1,n+1):
    data[i][j]+=(data[i-1][j]+ data[i][j-1]- data[i-1][j-1])

result=-sys.maxsize

for k in range(n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i+k>n or j+k>n:
        continue
      result= max(result, getSquareBenefit(i,j,k))
      #print(i,j, result)

print(result)