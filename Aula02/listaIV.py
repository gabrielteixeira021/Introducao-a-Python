"""
QUESTÃO 01: Faça um programa que leia um 
número  inteiro  positivo  N e  exiba  todos  os múltiplos de Y inferiores a N, onde N e Y são 
fornecidos pelo usuário.
"""

# Nota: 1,5/2,5 
# Não exibe os multiplos de Y, ao invés, exibe somente o valor de Y por iteração
N = int(input("Insira N: ")) # 10
Y = int(input("Insira Y: ")) # 2

i = Y 
# percorre o intervalo de Y a N 
while i < N:
    
    # Verificar se é multiplo
    if i % Y == 0:
        print(Y) # 2, 4, 6, 8  <- Trocar o print Y por i 
        print("É múltiplo: ")
    i+=1

"""
QUESTÃO 02: Faça um programa que exiba
todos os elementos da seguinte série, assim
como a soma destes elementos:
1, 50, 2, 49, 3, 48, 4, 47, 5, 46, ..., 49, 2, 50, 1
"""

# Nota: 2,5/2,5
p = 1
l = 50
o = p + l
som = 0

while p < 50 and l > 1:
    print(p, l, end=" ")
    som += o
    p+=1
    l-=1
print()
print(som, end="\n")

"""
QUESTÃO 03: Joãozinho investiu Q reais em
uma aplicação com rendimento fixo de R% ao
mês. Pede-se a implementação de um
programa que calcule o valor (e exiba-o)
disponível na conta de Joãozinho após A anos
de investimento.
"""

# Nota: 2,5/2,5
Q = int(input("Investimento Inicial:" ))
R = int(input("Rendimento Fixo: "))
A = int(input("Tempo de Investimento em Anos: "))
calculo_porcentagem = (R / 100) 
Montante = Q * (1 + calculo_porcentagem)**A
round(Montante, 2)
print(round(Montante, 2))

"""
QUESTÃO 04: Faça um programa que leia
300 números reais. Ao final, devem ser
exibidas as seguintes informações:
a) A quantidade de valores negativos
digitados;
b) A média dos valores positivos.
"""


# Nota: 2,25/2,5 
# Não seguiu a boa prática de colocar os nomes das variaveis de acordo com a regra universal da linguagem python -0,25 
Somaneg = 0
Somaposi = 0
Loga = 0

for x in range(300):
    numero = int(input("Insira um valor: "))
    if numero < 0:
        Somaneg += 1
    elif numero > 0:
        Somaposi += 1 
        Loga = Loga + numero
        Div = Loga / Somaposi

print("Quantidade de números negativos é: ", Somaneg)
print("A média é: ", Div)


# Aluno: Hércules Guia
# Nota final: 8.75
# Teste 1