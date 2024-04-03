#24516. 잘 알려진 수열 구하기

n= int(input())
result= [4*i-3 for i in range(1, n+1)]
print(*result)