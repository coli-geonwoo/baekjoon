#5545. 최고의 피자(실3)

topping_num = int(input())

dough_price, topping_price= map(int, input().split())

dough_calorie= int(input())
topping_calorie = [int(input()) for _ in range(topping_num)]
topping_calorie.sort(reverse=True)

result_calorie=dough_calorie
result_price= dough_price
result= dough_calorie/dough_price


for c in topping_calorie:
  if (result_calorie+c)/(result_price+topping_price)<result:
    break
  result_calorie+=c
  result_price+=topping_price
  result= result_calorie/result_price

print(int(result))
