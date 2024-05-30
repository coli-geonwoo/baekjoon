from bisect import bisect_right

n= int(input())
q=[]
nums= [int(input()) for _ in range(n)]

for i in nums:
  if q==0:
    q.append(i)
  else:
    idx= bisect_right(q, i)
    if idx==len(q):
      q.append(i)
    else:
      q[idx]=i

print(n-len(q))