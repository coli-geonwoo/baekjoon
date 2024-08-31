from collections import defaultdict

height =defaultdict(int)
n,h = map(int, input().split())
dp=[0]*(h+1)
cups = list(map(int, input().split()))

dp[0]=1

for c in cups:
    height[c]+=1

for i in range(1, h+1):
    temp=0
    for ch in height.keys():
        if i-ch <0:
            continue
        temp+= dp[i-ch] *height[ch]

    dp[i] = temp%1000000007

#print(dp)
print(dp[h])