import sys
input = lambda: sys.stdin.readline().strip('\n')
n= int(input())

kit = list(map(int, input().split()))

avg = sum(kit)//n

result= 0 

for i in range(n):
  if i==n-1:
    break
  diff = abs(avg-kit[i])
  if kit[i] < avg:
    kit[i+1]-=diff
  elif kit[i] > avg:
    kit[i+1]+=diff
  
  result+=diff
  #print(kit)
print(result)