T = int(input())
for test_case in range(1, T + 1):
    S = input()
    Y = S[:4]
    M = int(S[4:6])
    D = int(S[6:])
    A = 0
    if M == 2 :
        if D > 28 :
            A = -1
    else :
        if 0 < M <= 7 :
            if M%2 == 0 :
                if D > 30 :
                    A = -1
            else:
                if D > 31 :
                    A = -1
        elif 7 < M <= 12:
            if M%2 == 0 :
                if D > 31 :
                    A = -1
            else:
                if D > 30 :
                    A = -1
        else :
            A = -1
    if A == -1 :
        print("#{} -1".format(test_case))
    else : print("#{} {}/{}/{}".format(test_case,Y,S[4:6],S[6:]))


