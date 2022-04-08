n, m = map(int, input().split())
result = 0
coins = []
for i in range(n):
    coin = int(input())
    if coin <= m:
        coins.append(coin)
for c in reversed(coins):
    num = m // c
    if num > 0:
        result += num
        m -= num * c
print(result)