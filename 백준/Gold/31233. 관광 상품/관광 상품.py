import sys
from collections import deque

q=[]
n= int(input())
nums = list(map(int, input().split()))

result=min(nums[0], nums[1])

for i in range(n-2):
    temp = nums[i:i+3]
    temp.sort()
    result = max(result, temp[1])


print(result)