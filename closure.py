"""
Closure:
O principal propósito é permitir que uma função acesse 
e "lembre-se" das variáveis do seu escopo externo, 
mesmo após esse escopo ter terminado. 
"""

# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica

# define o multiplicador
duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadruplica = criar_multiplicador(4)

# executa a multiplicação interna
print(duplica(20))
print(triplica(9))
print(quadruplica(6))