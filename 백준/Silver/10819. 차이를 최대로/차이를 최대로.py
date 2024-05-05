
from itertools import permutations

n= int(input())
nums= list(map(int, input().split()))

cases = list(permutations(nums, n))
result=0

for c in cases:
  temp=0
  for i in range(n-1):
    temp+=abs(c[i]-c[i+1])


  result= max(result, temp)

print(result)