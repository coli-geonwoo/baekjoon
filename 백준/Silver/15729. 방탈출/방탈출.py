import sys

input = lambda: sys.stdin.readline().strip('\n')

n= int(input())
switch=  list(map(int, input().split()))
cnt=0

for i in range(n):
    if switch[i]:
      switch[i]= not switch[i]
      if i+1<n:
        switch[i+1]= not switch[i+1]
      if i+2<n:
        switch[i+2]= not switch[i+2]
      cnt+=1

print(cnt)