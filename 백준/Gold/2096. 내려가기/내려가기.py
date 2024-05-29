#2096. 내려가기(골5)

n= int(input())

data = [list(map(int, input().split())) for _ in range(n)]


before=[[0]*3 for _ in range(2)]

for i in range(1, n+1):
  after = [[0]*3 for _ in range(2)]
  for j in range(3):
    if j==0:
      after[0][j] = min(before[0][j], before[0][j+1]) + data[i-1][j]
      after[1][j] = max(before[1][j], before[1][j+1]) + data[i-1][j]
    elif j==2:
      after[0][j] = min(before[0][j], before[0][j-1]) + data[i-1][j]
      after[1][j] = max(before[1][j], before[1][j-1]) + data[i-1][j]
    else:
      after[0][j] = min(before[0][j], before[0][j-1], before[0][j+1]) + data[i-1][j]
      after[1][j] = max(before[1][j], before[1][j-1], before[1][j+1]) + data[i-1][j]
  before=after

print(max(after[1]), min(after[0]))
 