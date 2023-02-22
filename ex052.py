numero = int(input('Digite um numero'))
total = 0
for x in range(1, numero+1):
    if numero % x == 0:
        total += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(x), end=' ')
print('\n\033[mO numero {} foi divisível {} vezes'.format(numero, total))

if total == 2:
    print('\033[mPrimo')
else:
    print('\033[mNao primo')


