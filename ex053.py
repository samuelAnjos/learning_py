# Verifica se palidromo
# apos a sopa
cont = 0
frase = str(input('Informe a palavra')).replace(' ', '')
texto = frase[::-1]
for c in range(len(frase)):
    if frase[c] == texto[c]:
        cont += 1
if cont == len(frase):
    print('eh, palidromo')
else:
    print('nao eh palidromo')

