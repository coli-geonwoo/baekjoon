#2143. 두 배열의 합

from bisect import bisect_left
from collections import defaultdict


t= int(input())

n= int(input())
nums1= list(map(int, input().split()))

d1 = defaultdict(int)

for i in range(1,n+1):
    number = nums1[i-1]
    d1[number]+=1
    #print(number, end = " ")
    for j in range(i+1,n+1):
      number+=nums1[j-1]
      d1[number]+=1
      #print(number, end=" ")

    #print()

m= int(input())
nums2= list(map(int, input().split()))
result=0

for i in range(1,m+1):
    number = nums2[i-1]
    result+= d1[t-number]
    for j in range(i+1,m+1):
      number+=nums2[j-1]
      result+= d1[t-number]


print(result)

