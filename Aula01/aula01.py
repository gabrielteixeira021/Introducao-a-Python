# Variaveis

idade = 16
velocidade = 3.5
letra = 'a'

nota1 = 10

print(nota1)
print(float(nota1))
print(f"Mostrando a idade: {idade} \n Mostrando a velocidade {velocidade}")

# Condicionais parte 1

if idade > 12:
    print("Já passou da validade. - Gomes, Daniel, 2025")
else:
    print("Ta boa ainda. - Gomes, Daniel, 2025 ")

# Condicionais parte 2
horario = 3 # horas    

if horario < 12:
    print("Bom dia")
elif horario < 18:
    print("Boa tarde")
else: 
    print("Boa noite")

# Condicionais "encurtadas"
a = 11
b = 13
print("A é maior que B") if a > b else print("B é maior que A")

#    && = and
#    || = or
#    == equals
#

# Loops

# While (exemplo: contagem decrescente)
i = 10
while(i > 0):
    print(f"Contagem: {i}")
    i -= 1

# For (exemplo: contagem crescente)
for x in range(10):
    print(f"Contagem: {x}")

# Fim da aula 01