"""
https://docs.python.org/pt-br/3/library/stdtypes.html

"""

string = 'Victor Miguez'
print(id(string))
# string[5] = 'ABC' não funcionaria pois string é um tipo imutável em Python
outra_variavel = f'{string[:5]}ABC{string[6:]}'

print(outra_variavel)

string = 'Victor Miguez' + ' Cardozo de Souza'
# Quando fazemos a concatenação acima, um novo objeto é criado e colocado na variável string. podemos ver isso pelo endereço alocado na memória utilizando id().

print(string)
print(id(string))