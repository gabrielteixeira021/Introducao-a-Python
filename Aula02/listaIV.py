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


#exercício 5
for x in range(50):
    if (x % 2) == 0:
        print(x*-1, end=(", "))
    else: print(x, end=(", "))

#exercício 6
numero = int(input("Coloque um número aqui: "))


if numero <= 18:
  for x in range(1, 100):
    if ((x//10) + (x%10)) == numero: #Pedi ajuda ao copilot e o erro todo da questão foi uma /, tinha posto / e era //.
      print(x)
else: print("Error, Tente novamente")

#exercícios 7
entrevistados = int(input("Quantos entrevistados?: ")) #Utilizei GPT para identificar o meu erro de não indentar i IF dentro do FOR e esquecer o () no .lower()

feedback_positivo_masculino = 0
feedback_positivo_feminino = 0
feedback_negativo_masculino = 0
feedback_negativo_feminino = 0
for x in range(entrevistados):
  genero = input("Qual seu gênero?: ").lower()
  feedback = input("Gostou ou Não Gostou?: ").lower()
  if feedback == "gostou" and genero == "h":
    feedback_positivo_masculino += 1
  elif feedback == "gostou" and genero == "m":
    feedback_positivo_feminino += 1

  elif feedback == "não gostou" and genero == "h":
    feedback_negativo_feminino += 1
  elif feedback == "não gostou" and genero == "m": 
    feedback_negativo_feminino += 1

print("Quantidade de pessoas que gostaram do produto foi:", feedback_positivo_masculino + feedback_positivo_feminino)
print("Quantidade de pessoas que não gostaram do produto foi:", feedback_negativo_masculino + feedback_negativo_feminino)
if feedback_positivo_masculino > feedback_positivo_feminino:
  print("Homens tiveram uma maior aceitação sendo:", feedback_positivo_masculino, "contra", feedback_positivo_feminino)
elif feedback_positivo_masculino == feedback_positivo_feminino:
  print("Não houve diferença entre os gêneros!")
elif feedback_positivo_masculino < feedback_positivo_feminino:
  print("Mulheres tiveram uma maior aceitação sendo:", feedback_positivo_feminino, "contra", feedback_positivo_masculino)

  #exercícios 8
  ingresso_idade = 0
soma_salario_homem = 0
genero_feminino = 0
genero_masculino = 0

for x in range(250):
  matricula = input("Digite sua matrícula: ")
  genero = input("Sexo: ").lower()
  idade = int(input("Digite sua idade: "))
  salário = float(input("Digite seu salário: "))
  tempo = int(input("Digite quanto tempo está na empresa em anos: "))
  
  ingresso_idade_calculo = idade - tempo
  
  if genero == "m" or genero == "mulher":
    genero_feminino += 1
  elif genero =="h" or genero == "homem":
    genero_masculino += 1
    soma_salario_homem += salário

  if ingresso_idade_calculo <= 21:
    ingresso_idade += 1


media_salario_homem = soma_salario_homem/genero_masculino

print(ingresso_idade)
print(genero_feminino)
print(media_salario_homem) 
#Resposta abaixo do GPT pois não tive conhecimento ou lógica para fazer esse
''''
def main():
    ingresso_menor_21 = 0
    genero_feminino = 0
    soma_salario_homem = 0.0
    qtd_homens = 0

    matricula_mais_antigo = None
    matricula_mais_novo = None
    maior_tempo = -1
    menor_tempo = float("inf")

    for _ in range(250):
        matricula = input("Digite sua matrícula: ")
        genero = input("Sexo (h/m): ").lower()
        idade = int(input("Digite sua idade: "))
        salario = float(input("Digite seu salário: "))
        tempo = int(input("Tempo na empresa (anos): "))

        idade_ingresso = idade - tempo

        if idade_ingresso < 21:
            ingresso_menor_21 += 1

        if genero in ["m", "mulher"]:
            genero_feminino += 1
        elif genero in ["h", "homem"]:
            qtd_homens += 1
            soma_salario_homem += salario

        if tempo > maior_tempo:
            maior_tempo = tempo
            matricula_mais_antigo = matricula

        if tempo < menor_tempo:
            menor_tempo = tempo
            matricula_mais_novo = matricula

    media_salario_homem = soma_salario_homem / qtd_homens if qtd_homens > 0 else 0

    print("Funcionários que ingressaram com menos de 21 anos:", ingresso_menor_21)
    print("Quantidade de mulheres:", genero_feminino)
    print("Média salarial dos homens:", media_salario_homem)
    print("Matrícula do mais antigo:", matricula_mais_antigo)
    print("Matrícula do mais novo:", matricula_mais_novo)
'''