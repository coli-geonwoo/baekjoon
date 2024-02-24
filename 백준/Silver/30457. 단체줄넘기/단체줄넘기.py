n= int(input())
player= list(map(int, input().split()))
player_cnt={}

for i in player:
  if i not in player_cnt.keys():
    player_cnt[i]=1
  elif player_cnt[i]<2:
    player_cnt[i]+=1

print(sum(player_cnt.values()))