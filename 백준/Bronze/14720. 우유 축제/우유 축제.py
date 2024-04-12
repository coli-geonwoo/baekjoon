n= int(input())
milk=0
k= list(map(int, input().split()))
result=0
    
while(k):
    if milk not in k:
        break
    k= k[k.index(milk):]
    k.pop(0)
    result+=1
    milk= (milk+1)%3
print(result)