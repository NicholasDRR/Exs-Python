perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 10-5?',
        'Opções': ['15', '44', '7', '5'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['5', '25', '55', '50'],
        'Resposta': '5',
    }
]

for items in perguntas:
    print(f"Pergunta: {items['Pergunta']}")
    print()
    print('Opções:')
    
    for i, options in enumerate(items['Opções']):
        print(f'{i}) ', options)
        
    answer = input('Escolha uma opção: ')
    
    if answer == items['Resposta']:
        print('Você acertou!')
        print()
    else:
        print('Você errou!')
        print()