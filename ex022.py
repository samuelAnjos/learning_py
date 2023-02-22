nome = str(input('Informe o nome completo, por favor'))
print(nome.upper())
print(nome.lower())

nomeSemEspaco = nome.replace(' ', '')
print(len(nomeSemEspaco))

nomeDividido = nome.split()
nomePosicao = len(nomeDividido[0])
print('QUANTIDADE DA PRIMEIRA FRASE {}'.format(nomePosicao))


