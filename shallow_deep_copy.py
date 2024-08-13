# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy # o import copy traz o método copy.deepcopy() que copia tudo.

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# da forma abaixo, d2 recebe o ponteiro para d1,
# e toda modificação em d2 será atribuída em d1
# (e vice-versa).
# d2 = d1

# utilizando o método copy, fazemos uma shallow copy,
# onde *tudo o que for mutável* receberá apenas o ponteiro
# para o valor e, portanto, caso mexa-se neste
# valor mutável, o mesmo será alterado em todos os dicts
d2 = d1.copy() # shallow copy

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)