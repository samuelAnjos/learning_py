fibonacci = int(input('Informe um numero'))

x=1
i=2
y = 0
print(y, end=' ')
print(x, end=' ')
while i < fibonacci:
    f = x + y
    print(f, end=' ')
    y = x
    x = f
    i+=1