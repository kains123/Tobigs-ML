import numpy as np
def start_B(graph):
  all_arr = []
  for i in range(8):
    row_arr = []
    if i == 0:
      now_t = "R" #밑에서 같으면 바꿔주니까 "B"가 아닌 "R"로 설정
      first_row_t = "B" #이전 row의 첫번 째를 나타내줌
    else:
      if first_row_t == "B":
        now_t = "B" #밑에서 같으면 바꿔주니까 "R"가 아닌 "B"로 설정
        first_row_t="R"
      else:
        now_t = "R" #밑에서 같으면 바꿔주니까 "R"가 아닌 "B"로 설정
        first_row_t="B"
    for j in range(8): 
      if graph[i][j] == now_t: #이게 다르면 그대로 같으면 바꿔줘야함.
        row_arr.append(1)
        if now_t == "B" : 
          now_t = "R"
        else: 
          now_t = "B"
      else:
        row_arr.append(0)
        now_t = graph[i][j]
    all_arr.append(row_arr)
  
  all=np.array(all_arr)
  return all.sum()

def start_R(graph):
  all_arr = []
  for i in range(8):
    row_arr = []
    if i == 0:
      now_t = "B" #밑에서 같으면 바꿔주니까 "R"가 아닌 "B"로 설정
      first_row_t = "R" #이전 row의 첫번 째를 나타내줌
    else:
      if first_row_t == "B":
        now_t = "B" #밑에서 같으면 바꿔주니까 "R"가 아닌 "B"로 설정
        first_row_t="R"
      else:
        now_t = "R" #밑에서 같으면 바꿔주니까 "R"가 아닌 "B"로 설정
        first_row_t="B"
    for j in range(8): 
      if graph[i][j] == now_t: #이게 다르면 그대로 같으면 바꿔줘야함.
        row_arr.append(1)
        if now_t == "B" : 
          now_t = "R"
        else: 
          now_t = "B"
      else:
        row_arr.append(0)
        now_t = graph[i][j]
    all_arr.append(row_arr)
        
  all=np.array(all_arr)
  return all.sum()

def cut_group(graph, n, m):
  arr = np.array(graph)
  width_left = m-8 
  height_left = n-8
  sum_list = []
  for i in range(height_left+1):
    for k in range(width_left+1):
      sum_list.append(start_R(arr[i:i+8, k:k+8]))
      sum_list.append(start_B(arr[i:i+8, k:k+8]))
  sum_list.sort()
  return sum_list[0]


graph = []
n, m= map(int, input().split())
for _ in range(n):
    graph.append(list(map(list,input().split())))
    list2 = sum(graph, [])
result = cut_group(list2, n, m)
print(result)