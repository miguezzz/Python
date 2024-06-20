"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a # lista_b passa a apontar para o mesmo enderço que lista_a

lista_b[0] = 'Qualquer coisa' # mexendo em b, a também será modificada
print(lista_a)
print(lista_b)

lista_c = ['Luiz', 'Maria', 1, True, 1.2]
lista_d = lista_c.copy() # retorna cópia da lista para a variável

lista_c[0] = 'Qualquer coisa'
print(lista_c)
print(lista_d)