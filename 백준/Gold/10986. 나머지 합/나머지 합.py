from collections import defaultdict
import math

n,k= map(int, input().split())

data = list(map(int, input().split()))

cur_sum = [0] *(n+1)
mod_map = defaultdict(int)

for i in range(1, n+1):
    cur_sum[i] = (cur_sum[i-1]+ data[i-1])%k
    mod_map[cur_sum[i]]+=1

#print(cur_sum)
#결국 두 숫자의 comb(n,2)만큼 나옴
result=mod_map[0]

for key in mod_map.keys():
    result+=math.comb(mod_map[key],2)

print(result)


