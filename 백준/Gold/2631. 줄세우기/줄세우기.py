import sys 

input = lambda: sys.stdin.readline().strip('\n')

n= int(input())
dp=[1]*n

nums= [int(input()) for _ in range(n)]


for i in range(1, n):
  for j in range(i):
    if nums[i] > nums[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))