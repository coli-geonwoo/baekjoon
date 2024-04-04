#23254. 나는 기말고사형 인간이야(골5)

import heapq
import sys
#input = lambda: sys.stdin.readline().strip('\n')
n,m= map(int, input().split())

time= n*24

base_score= list(map(int, input().split()))
score = list(map(int, input().split()))

q=[]
for i in range(m):
  heapq.heappush(q, (-score[i], base_score[i], i))

while(q and time>0):
  up, base, idx= heapq.heappop(q)
  up=-up

  #할 수 있는 만큼 올리기
  t= min(time, (100-base)//up)
  time-=t
  base_score[idx] += t*up

  if base_score[idx] <100 and 100-base_score[idx] <up:
    heapq.heappush(q, (base_score[idx]-100, base_score[idx], idx))
  #print(base_score, up, base, idx, t)
  #print()

print(sum(base_score))