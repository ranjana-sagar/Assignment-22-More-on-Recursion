def adddigitN(N):
    if N//10==0:
        return N
    s=N%10+adddigitN(N//10)
    return s
