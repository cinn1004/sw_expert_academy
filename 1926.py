N = int(input())
for i in range(1,N+1):
    A = str(i).count("3") + str(i).count("6") + str(i).count("9")
    if  A > 0:
        print(A*'-',end = " ")
    else : print(i, end =" ")
    