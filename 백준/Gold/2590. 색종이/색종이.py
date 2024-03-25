
from collections import deque

paper= [0] + [int(input()) for i in range(6)]

result=paper[6] # 6x6은 그대로 하나의 색종이를 써야함

while(paper[5]):
  paper[1]-= min(11, paper[1]) # 최대 11개까지 넣을 수 있음
  paper[5]-=1
  result+=1


while(paper[4]):
  total=16
  paper[4]-=1
  result+=1
  total += 4*min(5, paper[2])
  paper[2] -= min(5, paper[2]) #최대 4개까지 넣을 수 있음
  paper[1] -= min( 36-total ,paper[1])

while(paper[3]):
  if paper[3]>=4:
    paper[3]-=4
  elif paper[3]==3:
    total= 27
    paper[3]-=3
    total+= min(paper[2],1)*4
    paper[2]-= min(paper[2], 1)
    paper[1]-= min(36-total, paper[1])
  elif paper[3]==2:
    total = 18
    paper[3]-=2
    total+= min(paper[2], 3)*4
    paper[2]-= min(paper[2],3)
    paper[1]-= min(36-total, paper[1])
  elif paper[3]==1:
    total = 9
    paper[3] -=1
    total+= min(paper[2], 5) * 4
    paper[2]-=min(paper[2],5)
    paper[1]-= min(36-total, paper[1])
  result+=1

while(paper[2]):
  total = min(paper[2],9)*4
  paper[2]-=min(paper[2],9)
  paper[1]-= min(36-total, paper[1])
  result+=1

while(paper[1]):
  paper[1]-=min(36, paper[1])
  result+=1

print(result)