import sys
import math

input = lambda: sys.stdin.readline().strip('\n')
n= int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

result1=[]
result2=[]

left1=0
right1=n-1
left2=0
right2=n-1

for i in range(n):
  if i%2==0:
    result1.append(nums[left1])
    result2.append(nums[right2])
    left1+=1
    right2-=1
  else:
    result1.append(nums[right1])
    result2.append(nums[left2])
    left2+=1
    right1-=1
    
total1=0
total2=0

for i in range(n-1):
  total1+= abs(result1[i]- result1[i-1])
  total2+= abs(result2[i]- result2[i-1])

print(max(total1, total2))