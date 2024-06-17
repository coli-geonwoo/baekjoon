# 단말수열
import heapq
'''
- 단말노드 먼저
- 연결 될 때마다 하나씩 -1
'''
n= int(input())
nums = list(map(int, input().split()))
degree = [0]*(n+1)

degree[0]=-1

for i in nums:
  degree[i]+=1

node= [i for i in range(1, n+1) if degree[i]==0]

result=[]

for i in nums:
  e = heapq.heappop(node)
  degree[i]-=1
  if degree[i]==0:
    heapq.heappush(node, i)
  
  if e<i:
    result.append((e,i))
  else:
    result.append((i,e))


a= heapq.heappop(node)
b= heapq.heappop(node)
result.append((a,b))

result.sort()
for r in result:
  print(*r)
    
