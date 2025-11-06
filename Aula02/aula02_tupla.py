# Tuplas


# Revisa Rapida: Lista
exemplo_lista_vazia = []

exemplo_lista = ["guitarra", "violao", 1, 8.5, 2+10]

listaDavy = ["Receba", "Perceba", "Pereça", "Desista dos seus sonhos e morra", 69, 51, "69 + 51", 120]
listaMarkola = ["Pedro", "Isabela", "Patrícia", "Davy", "Sofia", "la ele", 87, 'B', 69, 'p', 87.5]
listaNoct = ["Pedrin", "Marcola", "Felps"]



# Como Inicializar a Tupla
exemplo_tupla = ("maçã", "Uva", "jubilei", 2, 99, "jubilei")
exemplo_tupla_vazia = ()

MyTupla = ("Apple", "Pie", 99, 12, 9.5)

TuplaMarkolas = ("Antissemitismo", "Preconceito", "Racismo", "Transfobia", 58, 'u', 69)

tupla_davy = ("When ai meti yu in de soma", "tchubarrabissaun", "ui fel in love", 11, 9)



# Como acessar e visualizar elementos em uma tupla

print(exemplo_tupla[0])

print(MyTupla[0])

print(tupla_davy[3])

print(TuplaMarkolas[2])

# Como iterar sobre os elementos

for item in exemplo_tupla:
    print(f"Exibindo o elemento: {item}")

for i in tupla_davy:
    print(f"Elemento: {i}")

for item in MyTupla:
    print(f"Exibindo my friends: {item}")

for item in TuplaMarkolas:
    print(f"exibindo a tupla do Markolas: {item}");


# Desafio: Converta uma tupla em lista, tente modifica-la e em seguida salve novamente na tupla
print(exemplo_tupla[1])
lista_temporaria = list(exemplo_tupla)
lista_temporaria[1] = "Ovo"
exemplo_tupla = tuple(lista_temporaria)
print(exemplo_tupla[1])



# Como adicionar um novo elemento

# Converter a tupla em lista, adicionar o elemento e converter de volta

# Como remover um elemento na tupla

# Transformar a tupla em lista, remover da lista o elemento e em seguida converter para tupla de volta

