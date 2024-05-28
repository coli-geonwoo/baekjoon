import math
from bisect import bisect_right
import sys
#input = lambda: sys.stdin.readline().strip('\n')

n,m, max_heongumak= map(int, input().split())

width = list(map(int, input().split()))

all_width=set()

for i in range(n):
  for j in range(n):
    if i==j or width[i]- width[j]==0:
      continue
    all_width.add(abs(width[i]- width[j]))

height =  list(set((list(map(int, input().split())))))
all_width = list(all_width)

all_width.sort()
height.sort()

h_left=0
h_right=m-1

result=0
flag=False

for h in height:
  w_left=0
  w_right= len(all_width)-1
  while(w_left<=w_right):
    w_mid = (w_left+w_right)//2
    w = all_width[w_mid]
    temp = w*h*0.5
    if temp<=max_heongumak:
      flag=True
      result= max(temp, result)
      w_left = w_mid+1
    else:
      w_right= w_mid-1

if flag==False:
  print(-1)
else:
  print(int(result*10)*0.1)