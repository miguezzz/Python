"""
Tipo tupla - Uma lista imutável
Duas maneiras de criar uma tupla:
-> Com parênteses
-> Sem nada: tpl = 'bolinho', 1, 'abacate'

"""
lista = ['Maria', 2, 'Luiz']
lista_para_tupla = tuple(lista)
# tupla_para_lista = list(lista_para_tupla)
print(lista_para_tupla[-1])
print(lista_para_tupla)

tpl = 'bolo', 14, True
print(tpl)

tpl2 = ()
print(tpl2)