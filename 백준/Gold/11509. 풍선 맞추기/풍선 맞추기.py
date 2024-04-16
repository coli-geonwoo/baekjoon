
n= int(input())
k= list(map(int, input().split()))

t=-1
arow=[]

for i in k:
  if i not in arow:
    arow.append(i-1)
  else:
    arow[arow.index(i)]-=1
  
#print(arow)
print(len(arow))