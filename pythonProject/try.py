
try:
    print(a)
except Exception as error:
    raise Exception('Mensagem de erro')
else:
    print('Nenhum erro')
finally:
    print('Execução finalizada')