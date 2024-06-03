from itertools import permutations

nums = [i for i in range(1, int(input())+1)]

p = list(permutations(nums, len(nums)))

p.sort()

for c in p:
  print(*c)