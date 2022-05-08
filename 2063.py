import statistics as st
T = int(input())
N = list(map(int,input().split()))
S_N = sorted(N)
print(S_N[T//2])