#팀, 경기수, 팀 번호

from itertools import product
from collections import defaultdict

n, m,k = map(int, input().split())

score = defaultdict(int)

ongoing = []

for _ in range(m):
  team1, team2, result = map(int, input().split())
  #결과에 따른 점수 올리기
  if result==1:
    score[team1]+=1
  elif result==2:
    score[team2] +=1
  else:
    ongoing.append((team1, team2))

cases = list(product([0,1], repeat= len(ongoing)))

if(len(score.values())==0):
  threshold=0
  max_team=-1
else:
  threshold = max(list(score.values()))
  max_team = max(score, key= score.get)
cnt=0

for c in cases:
  #하나의 케이스
  temp=defaultdict(int)
  for idx, i in enumerate(c):
    if i==0:
      if ongoing[idx][0] not in temp.keys():
        temp[ongoing[idx][0]] = score[ongoing[idx][0]]+1
      else:
        temp[ongoing[idx][0]]+=1
    else:
      if ongoing[idx][1] not in temp.keys():
        temp[ongoing[idx][1]] = score[ongoing[idx][1]]+1
      else:
        temp[ongoing[idx][1]]+=1

  if len(temp.keys())==0:
    team=-1
  else:
    team = max(temp, key= temp.get)
  #print(team)
  
  #원래 1등이었다면
  if k in temp.keys():
    my_score = max(temp[k], score[k])
    if k==max_team and k==team:
      cnt+=1
    elif k!=max_team and k==team:
      if(threshold > my_score):
        cnt+=1
  else:
    my_score = score[k]
    if k==max_team and my_score> temp[team]:
      cnt+=1



print(cnt)
      