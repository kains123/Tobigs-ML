from itertools import permutations

def is_prime_number(x): # 2부터 (x - 1)까지의 모든 수를 확인

  for i in range(2, x): # x가 해당 수로 나누어떨어지면
    if x % i == 0:
      return False
  return True

def game(arr):
  arr_all_sum = []
  for i in range(len(arr)):
    arr_list = list(permutations(arr, i+1))
    for j in arr_list: 
      arr_all_sum.append(int(''.join(j)))
  arr_all_sum = list(set(arr_all_sum))
  
  cnt = 0
  for k in arr_all_sum: 
    if (is_prime_number(k) and k != 0 and k != 1):
      cnt += 1
    
  return cnt

arr = []
n = input()
for i in n:
  arr.append(i)

result = game(arr)
print(result)
