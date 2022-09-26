from datetime import date


def voto(idade):
    necessidade = ''
    if idade < 0:
        necessidade = 'ERRO, IDADE INVÁLIDA.'
    elif idade < 16:
        necessidade = 'NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        necessidade = 'VOTO OPCIONAL.'
    else:
        necessidade = 'VOTO OBRIGATÓRIO.'
    return necessidade



idade = date.today().year - int(input('Em que ano você nasceu? '))
print(f'Com {idade} anos: {voto(idade)}')
