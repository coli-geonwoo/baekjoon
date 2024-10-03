#1300 : k번째 수

n = int(input())
k = int(input())

result= 1

left= 1
right = k

while(left<=right):
    mid = (left+right)//2

    cnt=0
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    #print(mid, cnt)
    if cnt==k:
        result=mid
        break

    if cnt < k:
        left = mid+1
    else:
        result= mid
        right= mid-1

min_diff = n*n

for i in range(1, n+1):
    temp = min(result//i,n) * i
    if(abs(min_diff) > abs(result- temp)):
        min_diff = result-temp

    if min_diff==0:
        break


print(result- min_diff)