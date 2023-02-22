print('='*20)
print('BANCO SAM')
print('='*20)
valor = int(input('Qual o valor a ser sacado? R$ '))

cinq = valor // 50 #pego int 50
restoCinq = valor % 50 #resto 50

vinte = restoCinq // 20 #pego int 20
restoVinte= restoCinq % 20 #resto 20

dez = restoVinte // 10 #pego int 10
restoDez = restoCinq % 10 #resto 10

um = restoDez // 1 #pego int 50


print(f'Total de {cinq} cedulas de R$50')
print(f'Total de {vinte} cedulas de R$20')
print(f'Total de {dez} cedulas de R$10')
print(f'Total de {um} cedulas de R$1')
