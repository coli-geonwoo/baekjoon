import heapq
import sys

# input = lambda: sys.stdin.readline().strip('\n')
# 우선순위 > 실행시간 > 번호

n = int(input())
q = []

for i in range(n):
    # 요청 시간, 우선순위, 실행 시간
    a, b, c = map(int, input().split())
    heapq.heappush(q, (a, -b, c, i))

result = []
temp_q = []
time = 0

while (q or temp_q):
    # 작업 우선순위 큐가 비었을 때 > 큐에서 하나 pop
    if len(temp_q) == 0:
        req_time, important, running_time, num = heapq.heappop(q)
        important = -important
        heapq.heappush(temp_q, (-1 * (important - req_time), running_time, num, req_time))

    # 우선순위가 높은 작업 하나를 선택한다.
    pim, prun, pnum, preq_time = heapq.heappop(temp_q)
    time = max(time, preq_time) + prun
    result.append(pnum + 1)

    while (q and q[0][0] <= time):
        req_time, important, running_time, num = heapq.heappop(q)
        important = -important
        heapq.heappush(temp_q, (-1 * (important - req_time), running_time, num, req_time))

print(*result)
