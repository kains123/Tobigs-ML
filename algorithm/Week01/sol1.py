from collections import deque

def game(graph):
    min_arr = []
    for i in graph: 
      min_arr.append(min(i))
    return max(min_arr)

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))
result = game(graph)
print(result)
