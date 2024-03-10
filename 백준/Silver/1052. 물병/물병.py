n,k= map(int, input().split())
answer=0

#필요한 물병의 개수가 k개 이상이라면
while(bin(n).count("1") > k):
  idx = bin(n)[::-1].index("1") #가장 오른쪽에 있는 1의 위치
  answer+=2**idx #
  n+=2**idx
  #print(bin(n))
  #print(answer)
  #print(n)

print(answer)