T = int(input())
for test_case in range(1, T + 1):
    N = map(int,input().split())
    sum = 0
    for j in N:
        if (j % 2) != 0:
            sum +=j
    print("#{} {}".format(test_case,sum))