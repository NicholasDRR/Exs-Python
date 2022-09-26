def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('-' * tam)



escreva('Teste teste teste')
escreva('Teste  teste')
escreva('Teste')