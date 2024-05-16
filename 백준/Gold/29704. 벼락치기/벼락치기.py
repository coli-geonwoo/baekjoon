# 29704. 벼락치기(골5)

q=[]

n,t= map(int, input().split())

for _ in range(n):
  q.append(list(map(int, input().split())))

total= sum([i[1] for i in q])

dp=[[0]*(t+1) for _ in range(n+1)]

for idx in range(1, n+1):
  weight= q[idx-1][0]
  value = q[idx-1][1]
  for capacity in range(1, t+1):
    if capacity<weight:
      dp[idx][capacity] = dp[idx-1][capacity]
    else:
      #print(idx, capacity, weight, value)
      dp[idx][capacity] = max(dp[idx-1][capacity], dp[idx-1][capacity-weight]+value)

print(total - dp[n][t])