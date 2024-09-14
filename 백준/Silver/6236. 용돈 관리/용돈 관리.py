#용돈 관리

# m번만 통장에서 돈을 빼서 쓸 수 있음
# K를 인출
# 뺀돈으로 하루를 보낼 수 있다면 -> 그대로 사용
# 없으면 남은 금액 집어넣고 K원 인출

import sys
n,m= map(int, input().split())
money= [int(input()) for _ in range(n)]

def isAnswer(k):
    cnt=0
    my_money=0
    for cost in money:
        if my_money < cost:
            if(cost%k ==0):
                c= cost//k
            else:
                c = (cost//k) +1
            my_money = c*k - cost
            cnt+=c
        else:
            my_money -=cost

        if cnt >m:
            return False
    return True


left=max(money)
right= sys.maxsize
result=sys.maxsize

while(left<=right):
    mid = (left+ right)//2

    if isAnswer(mid):
        result = mid
        right = mid-1
    else:
        left = mid+1

print(result)

