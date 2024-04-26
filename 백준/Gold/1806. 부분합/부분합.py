# 투포인터 => 예외상황 : 맨 처음 숫자 하나만으로 연속될 때

import sys

n,m= map(int, input().split())
nums = [0]+list(map(int, input().split()))

for i in range(1, n+1):
  nums[i]+=nums[i-1]

left=0
right=1

result=sys.maxsize

flag=False

while(left<=n and right<=n):
      k= nums[right]-nums[left]

      if k >= m :
        flag=True
        result=min(result, right-left)
        left+=1
      else:
        right+=1

if flag==False:
  print(0)
else:
  print(result)