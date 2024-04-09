from collections import Counter
import copy
import sys

input = lambda: sys.stdin.readline().strip('\n')

n= int(input())
nums =list(map(int, input().split()))
nums_copy = copy.deepcopy(nums)
counter = list(Counter(nums).most_common())
max_n = counter[0][1]

result = []

if max_n > int(n/2):
  print(-1)
else:
  for i in range(n):
      if(nums[i]==nums_copy[i]):
        for j in range(n):
          if nums[i]!=nums_copy[j] and nums[j]!=nums_copy[i]:
            nums_copy[i],nums_copy[j] = nums_copy[j], nums_copy[i]
  
  print(*nums_copy)
  