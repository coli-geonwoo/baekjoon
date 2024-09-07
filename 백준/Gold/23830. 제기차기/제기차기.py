from collections import deque

import sys

def shouldClean(k):
    total = 0
    for score in data:
        if score > k + r:
            total += score - p
        elif score < k:
            total += score + q
        else:
            total += score

    if total < s:
        return True
    return False


n = int(input())
data = list(map(int, input().split()))
p, q, r, s = map(int, input().split())

left = 1
right = 100001 + r

result = sys.maxsize

while (left <= right):
    mid = (left + right) // 2

    if (shouldClean(mid)):
        left = mid +1
    else:
        result = mid
        right = mid -1

if (result == sys.maxsize):
    print(-1)
else:
    print(result)
