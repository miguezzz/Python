"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
print('Bem Vindo(a) ao verificador de Cadastro de Pessoas Físicas (CPFs)!')
continuar = True
while continuar:
    cpf_formato = input('Digite o CPF (123.456.789-10): ')
    if len(cpf_formato) != 14:
        print('Digite o CPF no formato indicado.')
        continue
    cpf_numeros = ''

    for digito in cpf_formato:
        if digito.isdigit():
            cpf_numeros += digito
            
    print(cpf_numeros)
    contador = range(10, 1, -1)
    multiplicador_start = 10
    result_final = 0
    for indice in range(0, 9):
        result_final += float(cpf_numeros[indice]) * multiplicador_start
        multiplicador_start -= 1
        
    result_final *= 10
    modulo_divisao = result_final % 11

    primeiro_digito = 0 if modulo_divisao > 9 else modulo_divisao

    print('O primeiro digito é:', int(primeiro_digito))
    
# cpf_formato = '991.953.510-94'
# cpf_numeros = ''

# for digito in cpf_formato:
#     if digito.isdigit():
#         cpf_numeros += digito
        
# print(cpf_numeros)

# contador = range(10, 1, -1)
# multiplicador_start = 10
# result_final = 0
# for indice in range(0, 9):
#     result_final += float(cpf_numeros[indice]) * multiplicador_start
#     multiplicador_start -= 1
    
# result_final *= 10
# modulo_divisao = result_final % 11

# primeiro_digito = 0 if modulo_divisao > 9 else modulo_divisao

# print(int(primeiro_digito))