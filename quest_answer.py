# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    contador_acertos = 0
    
    # acessa as perguntas
    print(pergunta['Pergunta'])
    print('Opções:')
    
    # acessa a lista de opções e itera sobre elas
    for i in range(len(pergunta['Opções'])):
        print(i, ') ', pergunta['Opções'][i], sep='')
    
    # outra maneira:
    # opcoes = pergunta['Opções']
    # for i, opcao in enumerate(opcoes):
    #     print(f'{i})', opcao)
    # print()
        
    resposta = str(input('Escolha uma alternativa: '))
    
    # verifica a resposta dada com a resposta correta
    if pergunta['Opções'][int(resposta)] == (pergunta['Resposta']):
        contador_acertos += 1
        print('Acertou\n')
    else:
        print('Errou\n')
    
    print('Você acertou', contador_acertos, 'questões!')
    
# outra solução

# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')