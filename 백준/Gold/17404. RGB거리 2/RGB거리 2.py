import sys
import copy
INF= sys.maxsize
input= lambda: sys.stdin.readline().strip('\n')
dp1=[[0,0,0]]
dp2=[[0,0,0]]
dp3=[[0,0,0]]

n= int(input())

first= list(map(int, input().split()))
first1= [first[0],INF, INF]
first2= [INF, first[1], INF]
first3= [INF, INF,first[2]]

dp1.append(first1)
dp2.append(first2)
dp3.append(first3)


for _ in range(n-1):
  a= list(map(int, input().split()))
  dp1.append(a)
  dp2.append(copy.deepcopy(a))
  dp3.append(copy.deepcopy(a))

for i in range(2,n+1):
  for j in range(3):        
    if j==0:
      dp1[i][j]= dp1[i][j]+min(dp1[i-1][j+1], dp1[i-1][j+2])
      dp2[i][j]= dp2[i][j]+min(dp2[i-1][j+1], dp2[i-1][j+2])
      dp3[i][j]= dp3[i][j]+min(dp3[i-1][j+1], dp3[i-1][j+2])

    elif j==1:
      dp1[i][j]= dp1[i][j]+ min(dp1[i-1][j-1], dp1[i-1][j+1])
      dp2[i][j]= dp2[i][j]+ min(dp2[i-1][j-1], dp2[i-1][j+1])
      dp3[i][j]= dp3[i][j]+ min(dp3[i-1][j-1], dp3[i-1][j+1])

    else:
      dp1[i][j]= dp1[i][j]+ min(dp1[i-1][j-1], dp1[i-1][j-2])
      dp2[i][j]= dp2[i][j]+ min(dp2[i-1][j-1], dp2[i-1][j-2])
      dp3[i][j]= dp3[i][j]+ min(dp3[i-1][j-1], dp3[i-1][j-2])

dp1[n][0]=INF
dp2[n][1]=INF
dp3[n][2]=INF

result= min(min(dp1[n]), min(dp2[n]), min(dp3[n]))
print(result)
