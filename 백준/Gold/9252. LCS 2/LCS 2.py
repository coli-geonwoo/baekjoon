#9252. LCS 2(골4)

a= list(input())
b= list(input())
n1= len(a)
n2 = len(b)

dp=[[0]*(n1+1) for _ in range(n2+1)]

for i in range(1,n2+1):
  for j in range(1, n1+1):
    if a[j-1]== b[i-1]:
      dp[i][j]= dp[i-1][j-1]+1
    else:
      dp[i][j]= max(dp[i-1][j], dp[i][j-1])

total= dp[n2][n1]
result=[]

x=n2
y=n1
while(x!=0 and y!=0):
  if dp[x][y]==dp[x-1][y]:
    x-=1
    continue
  if dp[x][y]== dp[x][y-1]:
    y-=1
    continue
  result.append(b[x-1])
  x-=1
  y-=1

result.reverse()

print(total)
print(''.join(result))
  