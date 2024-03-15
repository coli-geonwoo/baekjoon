
from collections import deque

s= input()
p= deque(list(input()))

cnt=0
before=""

for i in range(len(p)):
  before+= p.popleft()
  if len(before)>0 and before not in s:
    cnt+=1
    #print(before)
    before= before[-1]

if(len(before)>0):
  cnt+=1

print(cnt)