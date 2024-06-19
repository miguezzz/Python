"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Para generalizar, basta trocar 'secret' por um input.
word = 'secret'
letters_guessed = ''

guess = False
while guess is False:
    letter = input('Digite uma letra: ')
    
    if len(letter) > 1:
        print('Digite apenas 1 letra.')
        continue
    
    if letter in word:
        if letter not in letters_guessed:
            letters_guessed += letter
        else:
            print('Letra já adivinhada.')
            continue

    word_guessed = ''
    for secret_letter in word:
        if secret_letter in letters_guessed:
            word_guessed += secret_letter
        else:
            word_guessed += '*'
    print(word_guessed)
    
    if word_guessed == word:
        guess = True
        
print(f'Parabéns! Palavra secreta descoberta: {word}')