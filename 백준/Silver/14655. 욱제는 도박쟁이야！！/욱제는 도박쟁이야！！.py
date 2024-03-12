n= int(input())

num1=[]
num2=[]

round1= list(map(int, input().split()))
round2= [-i if i>0 else i for i in list(map(int, input().split()))]

round1= map(abs, round1)

print(sum(round1)- sum(round2))