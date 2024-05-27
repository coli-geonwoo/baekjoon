n,day =map(int, input().split())

d=set()

for _ in range(n):
  k= int(input())
  for i in range(k, day+1, k):
    d.add(i)

print(len(d))