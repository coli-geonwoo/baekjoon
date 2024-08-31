import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip('\n')

n = int(input())
check = defaultdict(int)
nums = [0]*(n+1)
check[0]=1
for i in range(1, n+1):
    if(nums[i-1]- i <0 or check[nums[i-1]-i] ==1):
        nums[i] = nums[i-1]+i
        check[nums[i]] =1
        continue

    nums[i] = nums[i-1]-i
    check[nums[i]] = 1

print(nums[n])