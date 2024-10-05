# 32347. 시간을 돌리고 싶어

# 타임머신은 최대 k번 사용
# t일 전으로 돌아갈 수 있음 > 최소 1일
# i일에 전원이 공급되고 있어야 함

from bisect import bisect_left, bisect_right

n, k = map(int, input().split())

days = []

turns = list(map(int, input().split()))

for idx, i in enumerate(turns):
    if i == 1:
        days.append(idx + 1)

result = n-1

left = 0
right = n

while (left <= right):
    mid = (left + right) // 2

    flag = True
    start = n
    cnt = 0

    while (True):
        #print(start, mid)
        temp = max((start - mid), 1)
        cnt += 1

        if cnt > k:
            flag = False
            break

        if temp == 1:
            break

        idx = bisect_left(days, temp)
        next = days[idx]
        #print(start, mid, next, idx, days)

        if start == next:
            flag = False
            break
        start = next

    if flag:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
