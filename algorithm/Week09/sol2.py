n = int(input())
call_time = []
for i in range(n):
    start, finish = map(int, input().split())
    call_time.append([start, finish])
call_time = sorted(call_time, key=lambda a: a[0]) #start정렬
call_time = sorted(call_time, key=lambda a: a[1]) #fin 정렬
last = 0
cnt = 0
for i, j in call_time:
    if i >= last:
        cnt += 1
        last = j
print(cnt)