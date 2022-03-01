from itertools import permutations

def game(arr, m):
  arr.sort()
  arr_list = list(permutations(arr, 3))
  
  list_arr = []
  for i in range(len(arr_list)):
    list_sum = sum(arr_list[i])
    if list_sum <= m:
      list_arr.append(list_sum)
  
  return max(list_arr)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = game(arr , m)
print(result)
