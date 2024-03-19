import sys

input = lambda: sys.stdin.readline().strip('\n')

n= int(input())
number = list(map(int, input().split()))

two_idx=[]
three_idx = [[0,1,2], [0,1,3], [1,2,5], [0,2,4]]

for i in range(6):
  for j in range(6):
    if i+j==5 or i==j or [j,i] in two_idx:
      continue
    else:
      two_idx.append([i,j])
#print(two_idx)
total=sum(number)
two=[]
three=[]

for com in three_idx:
  tmp= [number[idx] for idx in com]
  three.append(sum(tmp))
  three.append(total-sum(tmp))

for com in two_idx:
  tmp= [number[idx] for idx in com]
  two.append(sum(tmp))

three_min=min(three)
two_min= min(two)
min_num= min(number)
result=0
if n==1:
  print(total-max(number))
else:
  result+= (4*three_min + (n-2)*4*two_min + (n-2)**2*min_num)
  result+= (n-1)* (4*two_min+ 4*(n-2)*min_num)
  print(result)
