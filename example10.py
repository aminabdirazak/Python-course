def getMultiple(n1,n2):
    a=n1;
    while a<=10:
        b=1
        while b<=n2:
            print(a*b,end="\t")
            b+=1
        print()
        a+=1
getMultiple(1,12)
