#5619. 세번째(실2)
# 브루트 포스로도 풀리는 문제? => 메모리 초과
# combinations? => 메모리 초과
# 4개만 따로 빼기 => 0

from itertools import combinations
import sys
input = lambda: sys.stdin.readline().strip('\n')
n= int(input())

nums= [int(input()) for _ in range(n)]
nums.sort()
nums= nums[:4]

nums_case =  list(combinations(nums, 2))
#print(nums_case)
nums_cases=[]
for i in nums_case:
  nums_cases.append(int(str(i[0])+ str(i[1])))
  nums_cases.append(int(str(i[1])+ str(i[0])))
nums_cases.sort()

print(nums_cases[2])
