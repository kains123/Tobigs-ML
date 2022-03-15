def game(num, cnt):
  if num % 3 == 0:
    return game(num // 3 , cnt +1)
  elif num % 4 == 0 & num % 3 == 2:
    return game(num // 2 , cnt +1)
  elif num == 1:
    return cnt
  else:
    return game(num -1 , cnt +1)

n = int(input())
cnt = 0 
