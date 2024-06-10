n= int(input())
if n<4:
  if n==1 or n==3:
    print("CY")
  else:
    print("SK")
else:
  dp= [0]*(n+1)
  dp[1]=1
  dp[3]=1

  for i in range(4, n+1):
    if  (dp[i-1]==1 or dp[i-3]==1):
      dp[i]=0
    else:
      dp[i]=1
  
  if dp[n]==0:
    print("SK")
  else:
    print("CY")