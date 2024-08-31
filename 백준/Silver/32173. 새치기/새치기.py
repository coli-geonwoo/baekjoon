import sys
input = lambda: sys.stdin.readline().strip('\n')

n= int(input())
s= [0] + list(map(int, input().split()))

dp=[0]*(n+1)
total=0

for i in range(1, n+1):
    dp[i]= max(dp[i-1], s[i]-total)
    total+=s[i]

print(dp[n])