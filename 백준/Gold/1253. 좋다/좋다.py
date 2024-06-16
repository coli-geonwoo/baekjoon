#1253. 좋다(골4)

# 투포인터를 활용하여 가능한지 확인

n= int(input())
nums = sorted(list(map(int, input().split())))
cnt=0
for i in range(n):
  target = nums[i]
  left = 0
  right = n-1
  while(left<right):
    if left==i:
      left+=1
      continue
    elif right==i:
      right-=1
      continue

    if nums[left] + nums[right] >target:
      right-=1
    elif nums[left] + nums[right] < target:
      left+=1
    else:
      cnt+=1
      break

print(cnt)