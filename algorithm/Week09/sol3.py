from collections import deque

weight_arr = map(int, input().split())
weight_limit = int(input())

weight_arr.sort()
weight_arr = deque(weight_arr)
weight = 0
cnt = 0
while weight_arr:
    bus
    weight = weight_arr.pop()
    if weight_arr and weight+weight_arr[0]<=weight_limit:
        weight_arr.popleft()
    weight = 0
    cnt+=1
answer = cnt
print(answer)

