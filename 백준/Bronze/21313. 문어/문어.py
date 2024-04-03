
num= int(input())

result=[]

for _ in range(num//2):
  result.append(1)
  result.append(2)

if num%2 !=0:
  result.append(3)

print(*result)