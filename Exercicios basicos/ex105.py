def notas(* nts, sit = True):
    r = dict()
    r['total'] = len(nts)
    r['maior'] = max(nts)
    r['menor'] = min(nts)
    r['media'] = sum(nts) / len(nts)
    if sit:
        if r['media'] <= 4:
            r['situacao'] = 'REPROVADO'
        elif r['media'] <= 6:
            r['situacao'] = 'RECUPERAÇÃO'
        else:
            r['situacao'] = 'APROVADO'
    return r




retorno = notas(10, 4, 0, 0, 0, sit = True)
print(retorno)
