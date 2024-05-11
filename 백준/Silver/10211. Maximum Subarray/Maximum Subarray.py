import sys
t= int(input())

for _ in range(t):
    n= int(input())
    nums = [0]+ list(map(int, input().split()))
    for i in range(1, n+1):
      nums[i]+= nums[i-1]

    dp= [[0]*n for _ in range(n)]
    result= -sys.maxsize
    for i in range(1,n+1):
      for j in range(i, n+1):
        dp[i-1][j-1]= nums[j] - nums[i-1]
        result= max(result, dp[i-1][j-1])

    print(result)