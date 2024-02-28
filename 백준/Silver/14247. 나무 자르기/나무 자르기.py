n= int(input())

tree= list(map(int, input().split()))
grow= list(map(int, input().split()))
grow2= [(i, idx) for idx, i in enumerate(grow)]
grow2.sort()
result=0

for i in range(n):
  result+= tree[grow2[i][1]]+grow2[i][0]*i


print(result)
