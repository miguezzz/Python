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
    cpf_calculo = ''
    
    if len(cpf_formato) != 14:
        print('Digite o CPF no formato indicado.')
        continue
    cpf_numeros = ''

    for digito in cpf_formato:
        if digito.isdigit():
            cpf_numeros += digito
            
    print('CPF inserido:', cpf_numeros)
   
    multiplicador_start = 10
    result_final = 0
    for indice in range(0, 9):
        cpf_calculo += cpf_numeros[indice]
        result_final += float(cpf_numeros[indice]) * multiplicador_start
        multiplicador_start -= 1
        
    result_final *= 10
    modulo_divisao = result_final % 11

    primeiro_digito = 0 if modulo_divisao > 9 else modulo_divisao

    print('O primeiro digito é:', int(primeiro_digito))

# Calculo do segundo dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF,
# MAIS O PRIMEIRO DIGITO,
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 11

# Ex.:  746.824.890-70 (7468248907)
#    11 10  9  8  7  6  5  4  3  2
# *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
#    77 40 54 64 14 24 40 36  0 14

# Somar todos os resultados:
# 77+40+54+64+14+24+40+36+0+14 = 363
# Multiplicar o resultado anterior por 10
# 363 * 10 = 3630
# Obter o resto da divisão da conta anterior por 11
# 3630 % 11 = 0
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta

# O segundo dígito do CPF é 0

    multiplicador_start = 11
    result_final = 0
    for indice in range(0, 9):
        result_final += float(cpf_numeros[indice]) * multiplicador_start
        multiplicador_start -= 1
    
    result_final += float(cpf_numeros[9]) * multiplicador_start
    result_final *= 10
    modulo_divisao = result_final % 11
    
    segundo_digito = 0 if modulo_divisao > 9 else modulo_divisao

    print('O segundo digito é:', int(segundo_digito))
    
    cpf_calculo_final = f'{cpf_calculo}{str(int(primeiro_digito))}{str(int(segundo_digito))}'
    print('CPF calculado:', cpf_calculo_final)
    
    if cpf_calculo_final == cpf_numeros:
        print('CPF válido!')
    else:
        print('CPF inválido')
        
    prosseguir = input('Deseja prosseguir? [s/n]: ')
    
    if prosseguir == 's':
        ...
    else:
        print('Até logo...')
        continuar = False