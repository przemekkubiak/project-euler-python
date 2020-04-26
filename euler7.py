i=1
x=1
while True:
    if x%2==1:
        l=[n for n in range(1, x+1) if x%n==0]
        if len(l)==2:
            i+=1
            print(x)
    x+=1
    if i==10001:
        break
