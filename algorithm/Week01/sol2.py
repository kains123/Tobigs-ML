from collections import deque

def game(size, arr):
    x = 1
    y = 1
    for i in arr: 
      if i == 'R' and x < size: 
        x += 1
      elif i =='L' and x > 1: 
        x -= 1
      elif i =='U' and y > 1: 
        y -= 1
      elif i =='D' and y < size:
        y += 1
      else: 
        continue
    return str(y) + ' ' + str(x)



size = int(input())
arr = list(input().split())
result = game(size, arr)
print(result)

