# Variaveis

idade = 20
velocidade_media = 3.5
letra = 'a'

nota1 = 10

print(nota1)
print(float(nota1))
print(f"Mostrando a idade: {idade} \n Mostrando a velocidade {velocidade}")

# Condicionais parte 1

#Se chover mais tarde -> eu nao vou jogar bola


if idade > 18:
    print("Permitido comprar bebida")
else:
    print("Não Permitido comprar bebida")

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

#    && -> and
#    || -> or
#    == -> equals
#

# Loops

# While (exemplo: contagem decrescente)
g = 10
while g > 0:
    print(f"Contagem: {g}")
    g -= 1

# For (exemplo: contagem crescente)
for x in range(10):
    print(f"Contagem: {x}")

# Fim da aula 01