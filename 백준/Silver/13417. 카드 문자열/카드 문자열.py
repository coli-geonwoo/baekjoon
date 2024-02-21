t=int(input())

for _ in range(t):
  n= int(input())
  k= list(map(str, input().split()))
  if n==1:
    print(*k)
  else:
    result=k[0]
    for i in k[1:]:
      if result[0]>=i:
        result= i+result
      else:
        result+=i
    print(result)