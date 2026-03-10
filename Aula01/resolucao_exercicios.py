"""
# Exercício 1 – Variáveis e Tipos de Dados

1. Crie um programa que:

2. Peça ao usuário para digitar seu nome, idade e altura.

Mostre uma mensagem como esta:

``Olá [nome], você tem [idade] anos e mede [altura] metros.``

3. Converta a idade para inteiro e a altura para float antes de exibir.
"""

##exercício 1

nome = input("")
idade = int(input(""))
altura = float(input(""))

print(f"Olá", nome,",", "você tem", idade, "anos e mede", altura, "metros")

## Exercício 2 – Condicional Simples

#Peça para o usuário digitar uma nota (de 0 a 10).
#Depois, mostre:

#“Aprovado” se a nota for maior ou igual a 7

#“Recuperação” se a nota for entre 5 e 6.9

#“Reprovado” se a nota for menor que 5

Nota = float(input())

if Nota >= 7:
    print("Aprovado")
elif Nota <= 6.9 and Nota >= 5:
    print("Recuperação")
else: print("Reprovado")

##Exercício 3

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))

print("A é Tchunai") if a > b else print("B é Grandão")


"""
lista FAC
QUESTÃO 01: 
O custo ao consumidor de um carro novo é a 
soma do custo de fábrica com a porcentagem 
do distribuidor e dos impostos (aplicados ao 
custo  de  fábrica).  Desenvolver  um  algoritmo 
que  calcule  o  custo  ao  consumidor  de 
determinado carro.

--- Exemplo de entrada e saída ---

Entrada:
  Custo de fábrica: 50000
  Porcentagem do distribuidor (%): 10
  Porcentagem de impostos (%): 20

Cálculo:
  distribuidor = 50000 * (10 / 100) = 5000
  impostos     = 50000 * (20 / 100) = 10000
  custo_consumidor = 50000 + 5000 + 10000 = 65000

Saída:
  O custo ao consumidor é: R$ 65000.00

---

Outro exemplo:

Entrada:
  Custo de fábrica: 80000
  Porcentagem do distribuidor (%): 15
  Porcentagem de impostos (%): 25

Cálculo:
  distribuidor = 80000 * 0.15 = 12000
  impostos     = 80000 * 0.25 = 20000
  custo_consumidor = 80000 + 12000 + 20000 = 112000

Saída:
  O custo ao consumidor é: R$ 112000.00

"""


# Resolução
custo_fab = int(input("Custo de fabricação: "))
impostos = float(input("Impostos em (%): "))
distribuidora = int(input("Custo da distribuidora em (%): "))

impostos_calculo = custo_fab * (impostos / 100)
distribuidora_calculo = custo_fab * (distribuidora / 100)
valor_final = custo_fab + impostos_calculo + distribuidora_calculo

print("O valor do carro fica em:", valor_final)



"""
QUESTÃO 03: 
Construir um algoritmo que calcule o peso ideal 
de uma pessoa, de acordo com o seu gênero e 
altura, utilizando as seguintes fórmulas:   
x  para homens:   (72.7*h)-58 
x  para mulheres:   (62.1*h)-44.7
"""

# Entrada: Gênero: M | Altura: 1.75  →  Cálculo: (72.7 * 1.75) - 58 = 69.225
# Entrada: Gênero: F | Altura: 1.65  →  Cálculo: (62.1 * 1.65) - 44.7 = 57.765
# Saída: "Seu peso ideal é: 69.23 kg" / "Seu peso ideal é: 57.77 kg"

# resolução
altura = float(input("Qual sua altura?: "))
cromossomo = input("Insira tipagem cromossômica: ").upper()

if cromossomo == "XY":
    calculoxy = (altura * 72.7) - 58
    print("Seu peso ideal é:", calculoxy)
elif cromossomo == "XX":
    calculoxx = (altura * 62.1) - 44.7
    print("Seu peso ideal é:", calculoxx)
else: print("Utilize seu gênero XY (Masculino) ou XX (Feminino)")