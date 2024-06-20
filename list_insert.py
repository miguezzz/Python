"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete (CRUD)
Criar, ler, alterar, apagar = lista[i]
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Victor')
nome = lista.pop()
lista.append(1233)
del lista[-1] # elimina o último elemento
# lista.clear()
lista.insert(100, 5) # Mesmo que o índice 100 não exista, python não gera erros, mas coloca no fim da lista
print(lista[4]) # printa 5

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_concat = lista_a + lista_b
print(lista_concat)

lista_extend = lista_a.extend(lista_b) # extend() não retorna nada, apenas faz a ação
print(lista_extend) # printa None

lista_a.extend(lista_b) # estende pela segunda vez
print(lista_a) # printa [1, 2, 3, 4, 5, 6, 4, 5, 6]

lista_b.clear()
print(lista_b) # []