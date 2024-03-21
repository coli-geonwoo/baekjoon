
n= int(input())
height = [int(input()) for _ in range(n)]

k=[]
cnt=0

for i in height:
  if len(k)==0:
    k.append(i)
  while(len(k)>0 and k[-1]<= i):
    k.pop()
    #cnt+=1
    #print(k)
  cnt+=len(k)
  k.append(i)
  #print(k, i, cnt)
  #print()


print(cnt)