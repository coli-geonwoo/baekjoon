n,m,k = map(int, (input().split()))

data = [list(map(int, list(input()))) for _ in range(n)]
result=0
for i in range(n):
  temp=0
  for j in range(m):
    if data[i][j]==1:
      if temp>=k:
        result+=(1+(temp-k))
      temp=0
    else:
      temp+=1

    #print(i,j, temp, result)
  if temp>=k:
    result+=(1+temp-k)
  #print(data[i], result)

print(result)