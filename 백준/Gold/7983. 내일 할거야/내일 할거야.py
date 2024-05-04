import sys
import heapq


n= int(input())
q=[]
#d일이 걸리고 t일 안에 끝내야 함
day=[]

for _ in range(n):
  d,t = map(int, input().split())
  heapq.heappush(q, (-t, d))

start=sys.maxsize

while(q):
  end, duration = heapq.heappop(q)
  #print(end, duration)
  end=-end
  
  if start>end:
    start= end-duration+1
  else:
    start= start-duration
  #print(end, duration, start)

print(start-1)
