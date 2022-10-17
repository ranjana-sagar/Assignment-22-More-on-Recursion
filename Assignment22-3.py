def addevenN(N):
    if N==1:
        return 2
    s=N*2+addevenN(N-1)
    return s
