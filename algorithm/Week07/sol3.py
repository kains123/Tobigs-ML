def solution():
    n = int(input())
    num_list = [list(map(int,input().split())) for _ in range(n)]

    while len(num_list[-1]) != 1:
        new = []
        for i in range(0, len(num_list), 2):
            tmp = []
            for j in range(0, len(num_list), 2):
                calc = sorted([num_list[i][j], num_list[i+1][j], num_list[i]
                              [j+1], num_list[i+1][j+1]], reverse=True)
                tmp.append(calc[1])
            new.append(tmp)
        num_list = new
    print(num_list[0][0])


solution()