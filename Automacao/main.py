# https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga
import time
import pandas as pd
import pyautogui
import pyperclip

# Passo 1: Entrar no sistema (No caso o link)
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')  # Copiando link
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
# Esperando 5 segundos pro site carregar
time.sleep(5)
# Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta EXPORTAR)
pyautogui.click(x=332, y=289, clicks=2)
time.sleep(2)
# Passo 3: Download base de dados
pyautogui.click(x=468, y=298)  # Selecionando arquivo
pyautogui.click(x=1168, y=178)  # Clicando na barra de opc
pyautogui.click(x=898, y=633)  # Clicando download
time.sleep(5)
# Passo 4: Calcular os indicadores (faturamento, qtd de produtos)
tabela = pd.read_excel(r"E:\Downloads\Vendas - Dez.xlsx", engine="openpyxl")
quantidade = tabela['Quantidade'].sum()
faturamento = tabela['Valor Final'].sum()
# Passo 5: Entrar no email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('mail.google.com/mail/u/0/#inbox')  # Copiando link
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)
# Passo 6: Mandar um email para a diretoria com os indicadores
pyautogui.click(x=104, y=215)  # Clicar no botão +

# Escrever o destinatário
pyautogui.write('nicholasreis01@gmail.com')
pyautogui.press('tab')  # Selecionar email
pyautogui.press('tab')  # Selecionar Assunto

# Escrever assunto
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')  # Passar pra corpo do email

# Corpo do email
texto = f'''Boa noite
O faturamento foi de {faturamento:,.2f}
A quantidade de produtos foi {quantidade:,} 

Abs
Nicholas Ribeiro
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

# Enviando email
pyautogui.hotkey('ctrl', 'enter')
