def remove_star(size, x, y):
  global data

  if x+size>n or y+size>n:
    return

  start= size//3
  end =  (size*2)//3 -1

  for i in range(size):
    for j in range(size):
      if (i>=start and i<=end) and (j>=start and j<=end):
        data[x+i][y+j] =' '

def calculateK(x):
  k=0
  while(x!=1):
    x//=3
    k+=1
  return k

n= int(input())
data= [['*']*n for _ in range(n)]
k = calculateK(n)
sizes = [3**i for i in range(1, k+1)]
sizes.sort(reverse=True)

for size in sizes:
  for i in range(n):
    for j in range(n):
      if i%size==0 and j%size==0:
        remove_star(size, i, j)
        #for p in range(n):
          #print(*data[p])
        #print()

for i in range(n):
  print(''.join(data[i]))
