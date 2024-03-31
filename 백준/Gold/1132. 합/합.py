#1132. 합(골3)
import sys

input = lambda: sys.stdin.readline().strip('\n')
n= int(input())
number_cnt=[0]*10
nums = [i for i in range(10)]
none_zero=set()

for _ in range(n):
  k= list(input())
  num_len=len(k)-1
  for idx, i in enumerate(k):
    num= ord(i)-ord('A')
    if idx==0:
      none_zero.add(num)
    number_cnt[num] += 10**(num_len-idx)

can_zero = [i for idx, i in enumerate(number_cnt) if idx not in none_zero]

can_zero.sort()
can_zero.pop(0)

for i in none_zero:
  can_zero.append(number_cnt[i])

can_zero.sort()

result=0

for i in range(1,10):
  result+= i*can_zero[i-1]

print(result)