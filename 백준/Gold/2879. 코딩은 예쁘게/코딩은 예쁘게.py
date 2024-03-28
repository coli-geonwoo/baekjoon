n= int(input())

#현재 줄에 있는 탭의 개수
current_tab = list(map(int, input().split()))
hope_tab = list(map(int, input().split()))

diff = [hope_tab[i] - current_tab[i] for i in range(n)]
dp = [0] *n
dp[0]= abs(diff[0])

for i in range(1, n):
  #부호가 다를 때 => 방향이 다르기 때문에 두 방향 모두 더함
  if diff[i-1] *diff[i] <0:
    dp[i]= dp[i-1]+ abs(diff[i])
  # 더 많이 들여써야 할 때 => 추가분만 해주기
  elif abs(diff[i-1]) < abs(diff[i]):
    dp[i]= dp[i-1]+ (abs(diff[i])-abs(diff[i-1]))
  elif abs(diff[i-1]) >= abs(diff[i]):
    dp[i]= dp[i-1]

print(dp[n-1])