import sys
input = lambda: sys.stdin.readline().strip('\n')

result = sys.maxsize
result_idx = -1
n= int(input())

street_distance = list(map(int, input().split()))
left_distance = list(map(int, input().split()))
right_distance = list(map(int, input().split()))

right_distance.reverse()

for i in range(1, n-1):
  left_distance[i] += left_distance[i-1]
  right_distance[i] += right_distance[i-1]

right_distance.reverse()

left_distance = [0]+left_distance
right_distance= right_distance+[0]

#print(left_distance, right_distance)

for i in range(n):
  temp =street_distance[i]+left_distance[i]+right_distance[i]
  if result > temp:
    result=temp
    result_idx = i+1


print(result_idx, result)