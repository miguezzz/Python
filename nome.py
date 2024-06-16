# Exercício
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade: 
#     exiba "Desculpe, você deixou campos vazios."

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

if (len(nome) == 0 or len(idade) == 0):
    print('você deixou campos vazios!')
    breakpoint

nome_spaces = nome.count(' ')

print(f'seu nome invertido é {nome[::-1]}')
if (nome_spaces > 0):
    print(f'seu nome contém {nome_spaces} espaços')
else:
    print('seu nome não possui espaços')    

print(f'seu nome tem {len(nome) - nome_spaces} letras')
print(f'a primeira letra do seu nome é {nome[0]}')
print(f'a última letra do seu nome é {nome[-1]}')