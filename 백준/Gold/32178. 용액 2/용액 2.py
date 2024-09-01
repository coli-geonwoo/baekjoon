#D1 - 용액 : 투 포인터
import sys

n = int(input())
nums = [0] + list(map(int, input().split()))
data=[]

for i in range(1, n+1):
    nums[i]+= nums[i-1]
    data.append((nums[i], i))

data.sort()

result= data[0][0]
index= [0, data[0][1]]

for i in range(1, n):
    left = data[i-1]
    right = data[i]

    if abs(right[0]- left[0]) >= abs(result):
        continue

    if left[1]< right[1]:
        result = right[0]- left[0]
        index = [left[1], right[1]]
    else:
        result = left[0] - right[0]
        index = [right[1], left[1]]

    if abs(left[0]) < abs(result):
        result = left[0]
        index = [0, left[1]]

    if abs(right[0]) < abs(result):
        result = right[0]
        index = [0, right[1]]


    if result==0:
        break

index[0]+=1
print(result)
print(*index)