"""
Higher Order Functions
Funções de primeira classe
Basicamente utilizar função como outros tipos de dados.
Podem receber uma ou mais funções como argumentos;
Podem retornar uma função como resultado.

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes:

Higher Order Functions - Funções que podem receber e/ou retornar outras funções;
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...).
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Victor')
)
print(
    executa(saudacao, 'Boa noite', 'Miguez')
)


def criar_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

duplicar = criar_multiplicador(2) # atribui a função em duplicar
resultado = duplicar(5)  # Retorna 10
