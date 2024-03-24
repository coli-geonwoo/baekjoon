#25631. 마트료시카 합치기

n= int(input())
q = list(map(int, input().split()))
filled = [0]*n
q.sort()

for i in range(n-1):
  toy=q[i]
  for j in range(i+1, n):
    if toy< q[j] and filled[j]==0:
      filled[i]=-1
      filled[j]=1
      break
  #print(q)
  #print(filled)
  #print()

result=0
for i in filled:
  if i>=0:
    result+=1

print(result)

