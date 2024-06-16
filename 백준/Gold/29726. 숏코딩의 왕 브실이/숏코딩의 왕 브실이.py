#없앨 수 있는 찬스 M가지
#뒤에서부터 최댓값 갱신하여 생각해보기

import sys

INF = sys.maxsize
n,m= map(int, input().split())
nums = list(map(int, input().split()))

max_array=[0]*n
max_num= nums[-1]

for i in range(n-1, -1, -1):
  max_num = max(nums[i], max_num)
  max_array[i]=max_num

#print(max_array)
#앞은 작게, 뒤는 크게 유지
result=-INF

for i in range(m+1):
  start= nums[i]
  end = max_array[n-1 -(m-i)]
  result= max(result, end-start)

print(result)

