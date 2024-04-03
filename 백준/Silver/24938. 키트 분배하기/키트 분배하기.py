n= int(input())

kit = list(map(int, input().split()))

avg = sum(kit)//n

diff =  [avg-i for i in kit]+[0]


result=0

while(True):
  if len(set(diff))==1 and diff[0]==0:
    break
  
  plus_idx=-1
  minus_idx=-1
  cnt=0
  for i in range(n+1):
    if plus_idx !=-1 and minus_idx != -1:
      s = min(abs(diff[plus_idx]), abs(diff[minus_idx]))
      #print(diff[plus_idx], diff[minus_idx])
      diff[plus_idx] -=s
      diff[minus_idx]+=s
      result+= abs(plus_idx-minus_idx)*s
      break

    if diff[i]>0 and plus_idx==-1:
      plus_idx = i
      cnt+=1
    elif diff[i]<0 and minus_idx==-1:
      minus_idx= i
      cnt+=1
  #print(diff)

print(result)