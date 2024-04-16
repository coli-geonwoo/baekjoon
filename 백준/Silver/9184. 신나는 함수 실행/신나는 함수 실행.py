# 신나는 함수 실행


dp=[[[1]*(100) for _ in range(100)] for _ in range(100)]

for a in range(50, 100):
  for b in range(50,100):
    for c in range(50, 100):
      if a<b and b<c:
        dp[a][b][c]= dp[a][b][c-1]+ dp[a][b-1][c-1] - dp[a][b-1][c]
      else:
        dp[a][b][c]=dp[a-1][b][c]+ dp[a-1][b-1][c]+ dp[a-1][b][c-1]- dp[a-1][b-1][c-1]

        
while(True):
  a,b,c= map(int, input().split())
  if [a,b,c]==[-1,-1,-1]:
    break
  if a<=0 or b<=0 or c<=0:
    print("w({}, {}, {}) = {}".format(a,b,c,1))
  elif a>20 or b>20 or c>20:
    print("w({}, {}, {}) = {}".format(a,b,c,dp[69][69][69]))
  else:
    print("w({}, {}, {}) = {}".format(a,b,c,dp[a+49][b+49][c+49]))