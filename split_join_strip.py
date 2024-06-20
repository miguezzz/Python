"""
split, join e strip com list e str
split - divide uma string (list)
join - une uma string
strip - elimina espaços antes e depois das strings
rstrip - elimina espaços antes das strings
lstrip - elimina espaços depois das strings
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') # sem parâmetro: divide por espaços

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)