from itertools import combinations, permutations, product
from tkinter import *

pessoas = ['Luiz', 'Pedro', 'João', 'Gustavo']

for c in product(pessoas, repeat=2):
    print(c)


janela = Tk()

janela.title('Teste')
texto = Label(janela, text='Clique para executar')
texto.grid(column=0, row=0)
texto2 = Label(janela, text='Clique para executar2')
texto2.grid(column=1, row=0)
janela.mainloop()
