n=600851475143
i=1
l=[]
while i<=n:
    if n%i==0:
        m=[o for o in range(1, i+1) if i%o==0]
        if len(m)==2:
            l.append(i)
    i+=1
print(max(l))
