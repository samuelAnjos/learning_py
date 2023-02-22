preco = float(input('Valor do produto'))
condicaoPagamento = str(input('Qual condicao de pagamento: 1- Vista dinheiro cheque, '
                              '2- Vista cartao, 3- 2x no cartao, 4- 43x ou mais no cartao'))

if condicaoPagamento == '1':
    print('Valor do produto com desconto {}'.format(preco - (preco*10/100)))
elif condicaoPagamento == '2':
    print('Valor do produto com desconto {}'.format(preco - (preco * 5 / 100)))
elif condicaoPagamento == '3':
    print('Produto nao tem desconto {}'.format(preco))
else:
    print('Valor do produto com desconto {}'.format(preco + (preco * 20 / 100)))