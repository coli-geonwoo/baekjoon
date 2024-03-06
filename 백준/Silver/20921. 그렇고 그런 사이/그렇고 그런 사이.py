from collections import deque
import sys
input = lambda: sys.stdin.readline().strip('\n')

n, k= map(int, input().split())

q=deque([n])
q1=[]

nums= [i for i in range(n, 0, -1)]

for i in nums[1:]:
  if k>0:
    if k>len(q):
      q.append(i)
      k-=len(q)-1
    else:
      q.insert(k, i)
      k=0
  else:
    q1.append(i)

q1.reverse()
result= q1+list(q)

print(*result)