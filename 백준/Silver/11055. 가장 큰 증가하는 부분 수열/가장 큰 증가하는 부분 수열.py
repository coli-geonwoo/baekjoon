#11055. 가장 큰 증가하는 부분 수열(실2)

n = int(input())
nums = list(map(int, input().split()))
dp = [i for i in nums]

for i in range(1, n):
  for j in range(i):
    if nums[j]< nums[i]:
      dp[i]= max(dp[j]+nums[i], dp[i])

#print(dp)
print(max(dp))
      