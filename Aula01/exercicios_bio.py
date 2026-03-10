"""
# Exercicios Personalizados - Biomedicina e Reproducao Humana

# Exercicio 1 - Variaveis e Tipos de Dados

1. Crie um programa que:

2. Peca ao usuario para digitar o nome da paciente, a idade e a quantidade de foliculos observados no exame.

Mostre uma mensagem como esta:

``Paciente [nome], idade [idade] anos, apresentou [foliculos] foliculos no exame.``

3. Converta a idade e a quantidade de foliculos para inteiro antes de exibir.
"""

# resolucao
nome = input("")
idade = int(input())
qfoliculos = int(input())

print("Paciente", nome, "idade", idade, "anos,", "apresentou", qfoliculos, "no exame.")


"""
# Exercicio 2 - Condicional Simples

Em um acompanhamento inicial de reproducao humana, um exame mostrou a quantidade de ovocitos maduros coletados.

Crie um programa que peca esse valor ao usuario e depois mostre:

"Quantidade baixa" se o numero for menor que 5

"Quantidade adequada" se o numero for entre 5 e 10

"Quantidade alta" se o numero for maior que 10
"""

# resolucao

oocitos = int(input())

if oocitos < 10:
    print("Quantidade alta")
elif oocitos > 10 and oocitos < 5:
    print("Quantidade adequada")
else: print("Quantidade baixa")