#26646. 알프스 케이블카

n= int(input())
heights = list(map(int, input().split()))
result=0
for i in range(n-1):
  result += (heights[i] + heights[i+1])**2 + (heights[i]- heights[i+1])**2

print(result)
