#1082. 방 번호(골3)
import sys


n= int(input())

price = (list(map(int, input().split())))
number = [i for i in range(n)]
money = int(input())
dp=[-sys.maxsize]* (money+1)
result=[]

#뒤에서부터 숫자를 하나씩 고려
for i in range(n-1, -1, -1):
  number_price =  price[i]
  for j in range(number_price, money+1):
    #첫구입이라면 -> 구입하는게 이득 : number[i]
    #두번째 구입이라면 -> price이전의 숫자에서 현재 숫자를 붙인 숫자
    dp[j]= max(dp[j], dp[j-number_price]*10+number[i], number[i])
  #print(dp)
print(dp[money])
