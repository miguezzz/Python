# Unpacking
nomes = ['Levi', 'Hange', 'Berthold']
nome1, nome2, nome3 = nomes
print(nome2)

nome4, *resto = ['Reiner', 'Annie', 'Eren']
print(nome4, resto)

_, nome5, _ = ['Marco', 'Zeke', 'Armin']
print(nome5)