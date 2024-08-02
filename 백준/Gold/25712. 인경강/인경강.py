n,m = map(int, input().split())

columnCnts = list(map(int, input().split()))

nodes = set()

flag= True
for idx, cnt in enumerate(columnCnts):
  temp = set()
  col = list(map(int, input().split()))
  for i in range(0, cnt, 2):
    a= col[i]
    b= col[i+1]
    if idx==0:
      nodes.add((a,b))
      temp.add((a,b))
    else:
      for na, nb in nodes:
        if (a>=na and a<=nb) or (b>=na and b<=nb) or (a<=na<=b) or (a<=nb<=b):
          temp.add((a, b))

  if(len(temp)==0):
    flag=False
    break

  nodes = temp
      

if(flag):
  print("YES")      
else:
  print("NO")
    

  

