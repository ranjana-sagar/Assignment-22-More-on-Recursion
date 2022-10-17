def octN(N):
    if N<8:
        print(N)
    else:
        o=octN(N//8)
        print(N%8)
        
