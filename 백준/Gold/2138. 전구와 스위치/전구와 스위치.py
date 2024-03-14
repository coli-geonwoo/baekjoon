#2138. 전구와 스위치(골5)

import sys
import copy
#input = lambda:sys.stdin.readline().strip('\n')

#바꾸는 함수
def switch_on(light, i, n):
  for idx in (i-1, i, i+1):
    if idx>=0 and idx<n:
      light[idx]= abs(light[idx]-1)

n= int(input())
light= [int(i) for i in list(input())]
light1= copy.deepcopy(light)
target= [int(i) for i in list(input())]
cnt=0

result1=0
result2=1

#스위치를 누르지 않았을 때
for i in range(1, n):
    if(light[i-1]!= target[i-1]):
      result1+=1
      switch_on(light, i, n)
    #print(light)

#스위치 누르기
switch_on(light1, 0, n)

for i in range(1,n):
    if(light1[i-1]!= target[i-1]):
      result2+=1
      switch_on(light1, i, n)
    #print(light1)

flag1=True
flag2=True

light =list(map(str, light))
light1= list(map(str, light1))
target = list(map(str, target))

if ''.join(light) != ''.join(target):
  flag1=False
  result1= sys.maxsize

if ''.join(light1) !=''.join(target):
  flag2=False
  result2=sys.maxsize

if flag1==False and flag2==False:
  print(-1)
else:
  print(min(result1, result2))