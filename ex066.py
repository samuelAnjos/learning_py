sum = numero = contador = 0
while True:
    numero = int(input('Digite um numero (999 para parar)'))
    if numero == 999:
        break
    contador += 1
    sum += numero
print(f'A soma dos {contador} valores foi {sum}!')
