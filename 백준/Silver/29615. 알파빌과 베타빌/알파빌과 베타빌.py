#29615. 알파빌과 베타빌

from collections import deque

n,m= map(int, input().split())

w= list(map(int, input().split()))
w.reverse()
waiting = deque(w)
friends = list(map(int, input().split()))

result=0
cnt=0

while(waiting and waiting[-1] in friends):
  waiting.pop()
  cnt+=1

while(waiting and cnt !=m):
  for i in range(0, len(waiting)):
    if waiting[i] in friends:
      waiting[i], waiting[-1] = waiting[-1], waiting[i]
      result+=1
      break
  
  while(waiting[-1] in friends):
    waiting.pop()
    cnt+=1

print(result)
