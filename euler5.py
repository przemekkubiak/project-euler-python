x=116280
while True:
    i=1
    l=[]
    while i<21:
        if x%i==0:
            l.append(i)
            if len(l)==20:
                print(x)
        i+=1
    x+=116280
    if len(l)==20:
        break
