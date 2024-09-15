#25049. 뮤직 플레이 리스트

n= int(input())
music = [0] + list(map(int, input().split()))

dp1 = [0] * (n+2)
dp2 = [0] *(n+2)

for i in range(1, n+1):
    dp1[i] = max(dp1[i-1]+ music[i], music[i])

for i in range(n, -1, -1):
    dp2[i] = max(dp2[i+1] + music[i], music[i])

for i in range(1, n+1):
    dp1[i] = max(dp1[i-1], dp1[i])

for i in range(n, -1, -1):
    dp2[i] = max(dp2[i+1], dp2[i])

result = 0
#print(dp1)
#print(dp2)

for i in range(1, n+1):
    result = max(result, dp1[i] + dp2[i+1])
#print(result)
print(result+ sum(music))