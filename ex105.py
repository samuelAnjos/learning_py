def notas(* notas, sit=False):
    dic = dict()
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['media'] = sum(notas)/ len(notas)
    if sit:
        if dic['media'] >= 7:
            dic['situacao'] = 'Boa'
        elif dic['media'] >= 5:
            dic['situacao'] = 'Razoavel'
        else:
            dic['situacao'] = 'Ruim'

    return dic


resp = notas(5.5, 9.5, 10, sit=True)
print(resp)
