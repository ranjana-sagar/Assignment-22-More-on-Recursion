def fibN(N):
    if N==1:
        return 0
    elif N==2:
        return 1
    else:
        f=fibN(N-1)+fibN(N-2)
        return f
