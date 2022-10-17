def factoN(N):
    if N==1:
        return 1
    f=N*factoN(N-1)
    return f
