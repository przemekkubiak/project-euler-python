a=[i for i in range (100,1000)]
m=[x*y for x in a for y in a]
print(max(list(i for i in m if str(i)==str(i)[::-1])))
