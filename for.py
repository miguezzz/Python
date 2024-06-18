texto = input('Digite um texto: ')

texto_asterisco = ''
for letra in texto:
    texto_asterisco += f'*{letra}'
    print(letra)
    
print(f'{texto_asterisco}*')