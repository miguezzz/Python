"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []
while True:
    print('Selecione uma opção')
    selection = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
    if selection.startswith('i'):
        os.system('clear')
        lista_compras.append(input('Insira o item a ser adicionado: '))
    elif selection.startswith('a'):
        os.system('clear')
        print('Itens na lista:')
        for indice, item in enumerate(lista_compras):
            print(indice, item)
        try:
            del lista_compras[int(input('Qual item deseja remover? '))]
        except IndexError:
            print('Índice inexistente.')
        except ValueError:
            print('Por favor digite apenas números inteiros.')
        except Exception:
            print('Erro desconhecido.')
    elif selection.startswith('l'):
        os.system('clear')
        if not lista_compras:
            print('Não há itens na lista.')
        else:
            print('Itens na lista:')
            for indice, item in enumerate(lista_compras):
                print(indice, item)
    elif selection.startswith('s'):
        print('Até logo...')
        break
    else:
        print('Digite apenas opções disponíveis.')
        continue