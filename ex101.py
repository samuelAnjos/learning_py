def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual-ano
    if idade < 16:
        return 'Negado'
    elif 16 <= idade < 18 or idade > 65:
        return 'Opicional'
    else:
        return 'Obrigatório'

print(voto(2006))