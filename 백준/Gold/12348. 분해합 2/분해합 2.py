n= int(input())

start= max(n- 9*len(str(n)),1)
#print(start)

flag=True
for i in range(start, n):
  k= str(i)
  temp=i
  temp+=sum(list(map(int, list(k))))
  if temp==n:
    flag=False
    print(i)
    break

if flag:
  print(0)