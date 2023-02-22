number = ('zero','um','dois','tres','quatro','cinco',
          'seis','sete','oito','nove','dez','onze','doze','treze','quatorze'
          ,'quinze','dezesseis','dezessente','dezoito','dezenove','vinte')


while True:
    resposta = int(input('Digite um numero ente 0 e 20:'))
    if 0 <= resposta <= 20:
        break
print(f'Você digitou {number[resposta]}')