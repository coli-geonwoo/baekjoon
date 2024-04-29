from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip('\n')

n,m= map(int, input().split())

nums = [int(input()) for _ in range(n)]

nums.sort()
for _ in range(m):
  k= int(input())
  idx = bisect_left(nums, k)
  if idx>=n:
    print(-1)
  elif nums[idx]==k:
    print(idx)
  else:
    print(-1)
