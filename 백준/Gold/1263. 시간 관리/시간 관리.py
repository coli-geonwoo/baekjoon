import heapq
import sys

# 끝내야할 시간, 걸리는 시간

n= int(input())

q=[]
for _ in range(n):
  time, day = map(int, input().split())
  heapq.heappush(q, (-day, -time))

before = sys.maxsize

while(q):
  day, time = heapq.heappop(q)
  day= -day
  time = -time

  before = min(day-time, before-time)

if before<=0:
  print(-1)
else:
  print(before)