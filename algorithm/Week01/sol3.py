from collections import deque

def elevator(u, d, h):
    up_stair = u-d
    cnt = (h - u) // up_stair
    stair = cnt * up_stair
    while h > stair + u: 
      if stair < h: 
        stair += up_stair
        cnt += 1
    return cnt +1

graph = []
u, d, h = map(int, input().split())
result = elevator(u, d, h)
print(result)
