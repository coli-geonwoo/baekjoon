# 가장 긴 공통 부분 수열

a= input()
b= input()

dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]

result=0
for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
    if a[i-1]== b[j-1]:
      dp[i][j]= dp[i-1][j-1]+1
      result= max(dp[i][j], result)

print(result)
