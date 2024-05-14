
n= int(input())
number = list(map(int, input().split()))

number.reverse()
dp=[0]*n
result= []

dp=[0]*n
q=[]

for idx, i in enumerate(number):
  if len(q)==0:
    q.append(i)
    dp[n-1-idx]=-1
  else:
    flag=False
    while(q):
      if q[-1]>i:
        dp[n-1-idx]=q[-1]
        flag=True
        break
      q.pop()
    
    if flag==False:
      dp[n-1-idx]=-1
    
    q.append(i)

print(*dp)
