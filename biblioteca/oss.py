import os
# E:\Downloads
caminhoprocura = input('Digite um caminho: ')
termoprocura = input('Digite um termo: ')
conta = 0


def formata(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.', ',')


for raiz, diretorios, arquivos in os.walk(caminhoprocura):
    for arquivo in arquivos:
        if termoprocura in arquivo:
            try:
                conta += 1
                caminhocompleto = os.path.join(raiz, arquivo)
                nomearquivo, extarquivo = os.path.splitext(caminhocompleto)
                tamanho = os.path.getsize(caminhocompleto)
                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho', caminhocompleto)
                print('Nome: ', nomearquivo)
                print('Extensão: ', extarquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado: ', formata(tamanho))
            except PermissionError as error:
                print('Erro: ', error)
            except FileNotFoundError as error:
                print('Arquivo não encontrado: ', error)
            except Exception as error:
                print(error)

print()
print(f'{conta} arquivo(s) encontrados(s)')
