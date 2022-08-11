from Contas import conta
from Pessoas import pessoa

banco = conta.Banco()
cliente1 = pessoa.Clientes('Luiz', 30)
cliente2 = pessoa.Clientes('João', 30)
cliente3 = pessoa.Clientes('Joana', 30)
conta1 = conta.Poupanca(1111, 234145, 200)
conta2 = conta.Corrente(2222, 232143, 0)
conta3 = conta.Poupanca(1212, 234145, 0)
# INSERINDO CONTAS AOS CLIENTES
cliente1.inserir(conta1)
cliente2.inserir(conta2)
cliente3.inserir(conta3)
# INSERINDO CONTAS DOS CLIENTES NO BANCO
banco.inserir_contas(conta1)
banco.inserir_contas(conta2)
banco.inserir_contas(conta3)
# INSERINDO CLIENTES NO BANCO
banco.inserir_clientes(cliente1)
banco.inserir_clientes(cliente2)
banco.inserir_clientes(cliente3)
print('---------------------------------------')
if banco.autenticar(cliente1):
    cliente1.conta.sacar(10)
else:
    print('Cliente não autenticado')
print('---------------------------------------')
if banco.autenticar(cliente2):
    cliente2.conta.sacar(10)
else:
    print('Cliente não autenticado')
print('---------------------------------------')
if banco.autenticar(cliente3):
    cliente1.conta.sacar(10)
else:
    print('Cliente não autenticado')
print('---------------------------------------')