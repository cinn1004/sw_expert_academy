T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int,input().split()))
    answer = ''
    if N[0] == N[1] :
        answer = '='
    elif N[0] < N[1] :
        answer = '<'
    elif N[0] > N[1]:
        answer = '>' 

    print("#{} {}".format(test_case,answer))