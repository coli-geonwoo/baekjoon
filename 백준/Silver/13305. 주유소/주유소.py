#13305
# 이 선을 지나기 전까지의 min 값을 그 선에 곱해주어야 함
num= int(input())

line_list=list(map(int, input().split()))
oil_list=list(map(int, input().split()))

min_value=1000000001

for idx,i in enumerate(oil_list):
  if min_value > i:
    min_value=i
  oil_list[idx]= min_value

result=0

for i in range(num-1):
  result+=line_list[i]*oil_list[i]

print(result)