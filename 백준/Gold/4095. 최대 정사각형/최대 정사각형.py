
while(1):
    n,m= map(int, input().split())
    if n==0 and m==0:
      break

    data=[list(map(int, input().split())) for _ in range(n)]

    dp = [[0]*(m+1) for _ in range(n+1)]

    result=0

    for i in range(1, n+1):
      for j in range(1, m+1):
        if data[i-1][j-1]:
          # 옆, 위, 대각선 위 중 가장 짧은 정사각형을 기준으로 변의 길이를 늘림
          dp[i][j]= min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
          result= max(result, dp[i][j])
    
    print(result)