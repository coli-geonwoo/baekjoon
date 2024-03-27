import sys

cnt, demand= map(int, input().split())

q=[]
total_weight=0
for _ in range(cnt):
  weight, price = map(int, input().split())
  total_weight+=weight
  q.append((price, weight))

#가격은 오름차순, 무게는 내림차순
q.sort(key =lambda x:(x[0], -x[1]))

result = sys.maxsize


if total_weight<demand:
  print(-1)
else:
  temp=0
  same=0
  before_price = -1
  for i in range(cnt):
      price, weight = q[i]

      #같으면 추가 비용을 내야함
      if price==before_price:
        temp+=weight
        same+=price
      else:
        #더 비싸다면 이 가격에 지금까지의 고기를 모두 구매 가능
        temp+=weight
        before_price=price
        same=0
      
      if temp>=demand:
        result = min(result, price+same)

  print(result)