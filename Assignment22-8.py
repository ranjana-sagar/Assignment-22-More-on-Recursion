def binary(N):
    if N==1:
        print(1)
    else:
        binary(N//2)
        print(N%2)
