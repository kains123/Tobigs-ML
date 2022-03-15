def game(num):
  if num == 1:
    return 1
  elif num == 2:
    return 2
  elif num == 3:
    return 4
  else:
    return game(num-1) + game(num-2) + game(num-3)


n = int(input())
# arr = list(map(int, input().split()))
arr = []
for i in range(n):
  num =  int(input())
  arr.append(num)
result_arr = []
for num in arr:
  result = game(num)
  result_arr.append(result)

for i in result_arr:
  print(i)
