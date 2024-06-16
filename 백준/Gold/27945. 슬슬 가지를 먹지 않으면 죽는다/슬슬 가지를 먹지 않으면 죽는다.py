import heapq

def find_parent(x):
  global parent
  if x!= parent[x]:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_parent(a,b):
  global parent
  a= find_parent(a)
  b= find_parent(b)
  if a<b:
    parent[b] =a
  else:
    parent[a] =b


edges = []

n,m= map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
  a,b,cost = map(int, input().split())
  heapq.heappush(edges, (cost, a,b))

result=[]

while(edges):
  if len(result)==n-1:
    break
  
  cost, start, end = heapq.heappop(edges)

  if find_parent(start)!= find_parent(end):
    union_parent(start, end)
    heapq.heappush(result, cost)

#print(result)
day=1

while(result):
  if day== heapq.heappop(result):
    day+=1
  else:
    break

print(day)



  

