#14499
# 이동한 칸에 쓰여있는 점수가 0 > 점수 복사
# 0이 아니면 칸에 있는 수가 바닥면으로 복사됨

def move_up(dice):
  new_dice = [0]*6
  new_dice[0] = dice[1]
  new_dice[1] = dice[5]
  new_dice[2] = dice[2]
  new_dice[3] = dice[3]
  new_dice[4] = dice[0]
  new_dice[5] = dice[4]
  return new_dice

def move_down(dice):
  new_dice = [0]*6
  new_dice[0] = dice[4]
  new_dice[1] = dice[0]
  new_dice[2] = dice[2]
  new_dice[3] = dice[3]
  new_dice[4] = dice[5]
  new_dice[5] = dice[1]
  return new_dice

def move_right(dice):
  new_dice = [0]*6
  new_dice[0] = dice[2]
  new_dice[1] = dice[1]
  new_dice[2] = dice[5]
  new_dice[3] = dice[0]
  new_dice[4] = dice[4]
  new_dice[5] = dice[3]
  return new_dice

def move_left(dice):
  new_dice = [0]*6
  new_dice[0] = dice[3]
  new_dice[1] = dice[1]
  new_dice[2] = dice[0]
  new_dice[3] = dice[5]
  new_dice[4] = dice[4]
  new_dice[5] = dice[2]
  return new_dice

def roll_dice(direct, dice):
  if direct==1:
    return move_left(dice)
  elif direct==2:
    return move_right(dice)
  elif direct==3:
    return move_up(dice)
  else:
    return move_down(dice)

n,m,x,y,k = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
result=[]
dice = [0]*6
move = list(map(int, input().split()))
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

for direct in move:
  nx = x+dx[direct]
  ny = y+dy[direct]
  if nx<0 or nx>=n or ny<0 or ny>=m:
    continue
  dice = roll_dice(direct, dice)
  if(data[nx][ny]==0):
    data[nx][ny]=dice[0]
  else:
    dice[0]=data[nx][ny]
    data[nx][ny]=0
  
  result.append(dice[5])
  x,y = nx, ny

print(*result, sep="\n")
