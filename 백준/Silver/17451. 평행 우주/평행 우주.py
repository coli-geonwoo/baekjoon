import math
planet_num = int(input())

planet_speed = list(map(int, input().split()))

if planet_num==1:
  print(*planet_speed)
else:
  result_speed=[]
  planet_speed.reverse()
  max_speed= 0

  for speed in planet_speed:
    if max_speed >speed:
      max_speed=(math.ceil(max_speed/speed)*speed)
      result_speed.append(max_speed)
    else:
      result_speed.append(speed)
      max_speed=speed
  print(max(result_speed))