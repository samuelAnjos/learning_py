nome = str(input('Digite seu nome'))
nomeSplit = nome.split()
total = len(nomeSplit)-1
print('Seu primeiro nome = {}'.format(nomeSplit[0]))
print('Seu ultimo nome = {}'.format(nomeSplit[total]))
