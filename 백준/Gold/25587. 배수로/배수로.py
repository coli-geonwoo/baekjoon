#25587. 배수로(골3)
import sys

sys.setrecursionlimit(100000)

def find_parent(x):
  if x!= parent[x]:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_parent(a, b):
  global answer
  pa= find_parent(a)
  pb= find_parent(b)
  if pa==pb: #같은 그래프 내에 속할 경우
    return
  
  if(waters[pa-1] > dualibility[pa-1]):
    answer -= count[pa]
  
  if(waters[pb-1] > dualibility[pb-1]):
    answer-= count[pb]


  if pa<pb:
    parent[pb]=pa
    waters[pa-1]+= waters[pb-1]
    dualibility[pa-1] += dualibility[pb-1]
    count[pa]+=count[pb]
    if(waters[pa-1]> dualibility[pa-1]):
      answer+=count[pa]
  else:
    parent[pa]=pb
    waters[pb-1]+=waters[pa-1]
    dualibility[pb-1]+= dualibility[pa-1]
    count[pb]+= count[pa]
    if(waters[pb-1]> dualibility[pb-1]):
      answer+=count[pb]
    

def check():
  result=0

  for i in range(city_num):
    if dualibility[i] < waters[i]:
      result+=1
  
  return result

city_num, query_num = map(int, input().split())

dualibility = list(map(int, input().split()))
waters = list(map(int, input().split()))
count = [1]*(city_num+1)
parent = [i for i in range(city_num+1)]

answer = check()

for _ in range(query_num):
  query = list(map(int, input().split()))

  if(len(query)==1 and query[0]==2):
    print(answer)
  else:
    a= query[0]
    b= query[1]
    c= query[2]
    union_parent(b,c)

  #print(parent)
  #print(waters)
  #print(dualibility)
  #print()



