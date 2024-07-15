from collections import defaultdict

info = defaultdict(int)

n,m= map(int, input().split())
W, L, G = map(int, input().split())

for _ in range(m):
  a,b = input().split()
  if b=="W":
    info[a]=1

score=0
flag=False
for _ in range(n):
  a= input()
  if(info[a]==1):
    score+=W
  else:
    score = max(0, score-L)
  
  if score>=G:
    flag=True
    break

if flag:
  print("I AM NOT IRONMAN!!")
else:
  print("I AM IRONMAN!!")