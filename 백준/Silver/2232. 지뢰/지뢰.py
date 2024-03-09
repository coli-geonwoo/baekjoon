import sys
import copy
sys.setrecursionlimit(10000)

#input = lambda: sys.stdin.readline().strip('\n')

def bomb_explod(k):
  global bomb, cnt
  power = copy.deepcopy(bomb[k])
  bomb[k]=0
  bomb_exploded.append(k)
  bomb_left(k-1, power)
  bomb_right(k+1, power)

def bomb_left(k, power):
  global cnt,bomb
  if k<0:
    return
  
  if bomb[k]<power:
    bomb_exploded.append(k)
    power = bomb[k]

    if(k-1 not in bomb_exploded):
      bomb_left(k-1, power)
    bomb[k]=0

def bomb_right(k, power):
  global cnt,bomb
  if k>=n:
    return
  
  if bomb[k]<power:
    bomb_exploded.append(k)
    power =(bomb[k])
    if(k+1 not in bomb_exploded):
      bomb_right(k+1, power)
    bomb[k]=0

n = int(input())
bomb = [int(input()) for _ in range(n)]
bomb_exploded=[]
result=[]

while(max(bomb)!=0):
  idx = bomb.index(max(bomb))
  result.append(idx+1)
  bomb_explod(idx)

  #print(bomb)
  #print(bomb_exploded)

result.sort()
print(*result)
