# 수고르기

import sys

n,m= map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

left = 0
right =1

result=sys.maxsize

while(left<n and right<n):
  k = nums[right] - nums[left]
  
  if k>=m:
    result = min(result, k)
    left+=1
  else:
    right+=1

print(result)
  