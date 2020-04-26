m=[i for i in range(1, 101)]
x=[i**2 for i in m]
print(abs(sum(x)-(sum(m)**2)))
