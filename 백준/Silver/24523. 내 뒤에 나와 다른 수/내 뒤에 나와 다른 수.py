#24523. 내 뒤에 나와 다른 수(실2)
from collections import deque, defaultdict

number_indexs = defaultdict(deque)

n= int(input())
nums = list(map(int, input().split()))

for idx, i in enumerate(nums):
  number_indexs[i].append(idx+1)

result=[]

for idx, i in enumerate(nums):
  q= number_indexs[i]
  cnt=0
  while(q and q[0]-idx==1):
    q.popleft()
    cnt+=1
    idx+=1
  
  #print(idx)

  if idx==n:
    for _ in range(cnt):
      result.append(-1)
  else:
    for _ in range(cnt):
      result.append(idx+1)
  

print(*result)