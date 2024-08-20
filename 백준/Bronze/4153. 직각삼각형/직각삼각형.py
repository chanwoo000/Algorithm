while 1:
    a, b, c = map(int, input().split())
    if(a==0 & b==0 & c==0):
        break
    else:
        if (max(a,b,c)**2 == ((a**2 + b**2 + c**2) - max(a,b,c)**2)):
            print("right")
        else:
            print("wrong")

