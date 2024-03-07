n= int(input())
h= list(map(int, input().split()))

#h.sort()
result=0

for i in range(n-1):
  a= h[i]
  b= h[i+1]
  result+= (a**2+b**2)*2

print(result)