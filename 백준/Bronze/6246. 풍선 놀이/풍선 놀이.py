slot, t= map(int, input().split())


visited=[0]*(slot+1)

for _ in range(t):
  a,b= map(int, input().split())
  for i in range(a, slot+1, b):
    visited[i]=1

print(slot - sum(visited))