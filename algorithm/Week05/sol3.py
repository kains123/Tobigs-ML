def game(arr, max_arr):
  for i in range(3, n + 1):
    max_arr.append(max(max_arr[i - 1], max_arr[i - 3] + arr[i - 1] + arr[i], max_arr[i - 2] + arr[i]))
  return max_arr[n]


n = int(input())
arr = []
arr.append(0)
for i in range(n):
    arr.append(int(input()))
max_arr = []
max_arr.append(0)
max_arr.append(arr[1])
if n > 2:
  max_arr.append(arr[1] + arr[2])
  answer = game(arr,max_arr)
else:
  answer = sum(arr) 

print(answer)