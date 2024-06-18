nome = input('Digite seu nome: ')
nome_tamanho = len(nome)

print(nome)
print(nome_tamanho)

str_asterisco = ''
contador = 0
while (contador < nome_tamanho):
    str_asterisco += f'*{nome[contador]}'
    contador += 1

str_asterisco += '*'

print(str_asterisco)