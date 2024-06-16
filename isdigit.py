entrada_int = input('Digite um numero: ')
try:
    entrada_int = int(entrada_int)
    par = entrada_int % 2 == 0

    if par:
        par_impar_texto = 'par'
    else:
        par_impar_texto = 'ímpar'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')