def addN(N):
    if N==1:
        return 1
    s=N+addN(N-1)
    return s
