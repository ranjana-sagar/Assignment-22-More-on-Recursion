def addcubeN(N):
    if N==1:
        return 1
    s=N**3+addcubeN(N-1)
    return s
