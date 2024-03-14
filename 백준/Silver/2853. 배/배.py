# 2853. 배

n= int(input())
day= [ int(input()) for _ in range(n)]
cnt=0

for i in range(1, n):

  if day[i]==0:
    continue
  
  #print(day[i])
  
  flag=True
  
  k= day[i]- day[0]
  
  for j in range(1, n):
    if day[j]==0:
      continue
    if day[j]%k==1:
      flag=False
      day[j]=0
  if flag==False:
    cnt+=1

print(cnt)