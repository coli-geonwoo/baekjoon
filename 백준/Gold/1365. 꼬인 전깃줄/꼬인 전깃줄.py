
from bisect import bisect_left

n= int(input())

nums= list(map(int, input().split()))
dp=[nums[0]]

for num in nums:
  if dp[-1]<num:
    dp.append(num)
  else:
    idx = bisect_left(dp, num)
    dp[idx]=num

print(n-len(dp))

