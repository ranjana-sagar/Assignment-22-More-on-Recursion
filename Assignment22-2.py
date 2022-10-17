def addoddN(N):
    if N==1:
        return 1
    s=(N*2-1)+addoddN(N-1)
    return s
