### LIS bineary Search 활용
# 증가하면 추가
# 증가하지 않으면 이분탐색으로 위치 갱신

from bisect import bisect_left

n= int(input())

nums = list(map(int, input().split()))

dp=[nums[0]]

for num in nums:
  if num > dp[-1]:
    dp.append(num)
  else:
    idx = bisect_left(dp, num)
    dp[idx]=num

print(len(dp))