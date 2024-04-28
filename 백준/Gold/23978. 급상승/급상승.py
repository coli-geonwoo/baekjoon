def getSum(n,k):
  if k<=n:
    return (n+1)*k - k*(k+1)//2
  else:
    return n*(n+1)//2

n,k= map(int, input().split())

days= list(map(int, input().split()))
days.reverse()

d=[]

for i in range(n-1):
  d.append(days[i]- days[i+1])

left=0
right =k

result=0

while(left<=right):
  mid = (left+right)//2

  temp=getSum(mid, mid)

  for i in d:
    temp+=getSum(mid, i)
  #print(mid, temp)

  if temp>=k:
    #print(mid, temp)
    result=mid
    right=mid-1
  else:
    left =mid+1

print(result)
