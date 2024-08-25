#id, 번호, 점수가 시간 순대로 제출

#팀의 개수 n, 문제의 개수 k, 우리팀의 id, 로그 엔트리의 개수 m
# 팀 id, 문제 번호, 획득한 점수

from collections import defaultdict

t= int(input())
for _ in range(t):
    last_submit = defaultdict(int)
    cnt = defaultdict(int)
    total_score = defaultdict(int)

    n,k,team_id, m = map(int, input().split())

    dp=[[0]*(k+1) for _ in range(n+1)]

    for i in range(m):
      id, p_num, score = map(int, input().split())
      cnt[id]+=1
      last_submit[id]=i
      if(dp[id][p_num] <score):
        total_score[id] += score- dp[id][p_num]
        dp[id][p_num]=score


    result=[]

    for i in range(1, n+1):
      result.append((i, total_score[i], cnt[i], last_submit[i]))

    result.sort(key=lambda x:(-x[1], x[2], x[3]))

    #print(result)

    for idx, info in enumerate(result):
      id, score, cnt, last_submit = info
      if(id==team_id):
        print(idx+1)
        break

