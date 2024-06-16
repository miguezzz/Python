"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str

"""
variavel = 'Olá Mundo'
print(variavel[0:3]) #indice final nao eh incluso

#The step parameter is used to specify the steps to take from start to end index.
print(variavel[0:len(variavel):2])

#podemos inverter a string utilizando slice com passo negativo!
print(variavel[::-1])
#print(variavel[-1:-10:-1]) tambem funcionaria