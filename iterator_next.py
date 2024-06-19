"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
__ -> Dunder (Double Underscores)

"""
texto = 'Victor' # Iterável (objeto que possui os elementos)

# iterador = 'Victor'.__iter__()
iterador = iter(texto) # Iterador (objeto sabe iterar sobre os elementos)

while True:
    try:
        # print(iterador.__next__())
        print(next(iterador)) # Erro: StopIteration
    except StopIteration:
        break
    
########################################################
# "modo fácil" do que foi feito acima:
for letra in texto:
    print(letra)