a = 18
b = 0

try:
    print(b[0])
    c = a / (b + c)
    print(c)
except ZeroDivisionError as error:
    log_de_erros = error
    raise ZeroDivisionError('Você tentou dividir por 0')
except NameError:
    print('Nome de variável não definido')
except (TypeError, IndexError) as error:
    #print(error)
    #print(error.__class__.__name__)
    #print('TypeError + IndexError')   
    pass 
except Exception:
    print('Erro desconhecido.')
    
    
try:
    print(8 + 0)
except ZeroDivisionError:
    print('DIVIDIU POR 0')
else:
    print('Não deu erro')
finally:
    print('Sempre executado')
    
    
raise ValueError('DEU ERRO')