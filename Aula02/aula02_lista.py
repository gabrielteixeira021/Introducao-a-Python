
# Listas


# Como inicializar

# Inicializar com elementos dentro

lista_de_compras = ["Leite", "Macarrão", "Ovo", "Farofa", "Japonês", "Peixe", "Carne", "Frango"]

# Agora é com vocês

lista_fs = ["Percy Jackson", 0.12 ,"Eu Robo - Isac Isomov", 1.0, "Foco Roubado", 1.0]

lista_do_japones = ["Gilmore Girls", "O Diário de Uma Paixão", "Interestelar", "De Volta para o Futuro"]

lista_davy = ["Item 1", 2, "Alt+Z", 45.5]

# Inicializar uma lista vazia
lista_vazia = []
lista_vazia_fs = []
lista_vazia_japones = []
lista_vazia_davy = []

# Inicializar pelo contrutor 
lista_construtor = list(("Marcos", "Gabriel", "Fellype", "Davy"))

lista_construtor_fs = list(("Livre", "Compromisado", "Suspeitas", "Casado"))

list_gabriel = list(("Soso", "Isabela", "Samara"))

lista_construtor_davy = list(("Romano", "Hiragana", "Katakana", "Kanji", "Hangul", "Pying", "Cirílico", "Abjad"))

for itens, itens_b in zip(lista_construtor, lista_construtor_fs):
    print(itens + " - " + itens_b + "\n")

clear = lambda: print('\n' * 100)
clear()

# Como acessar/visualizar

# Como visualizar a estrutura completa
print(lista_construtor)

# Como visualizar um elemento específico

print(lista_de_compras[3])
print(lista_construtor_davy[-3])
print(lista_construtor[-1])

clear()
# Hi
print(lista_construtor[1])
print("Está interessado em: " + ", ".join(list_gabriel[:]))

# Como adicionar um novo elemento

# Append
lista_de_compras.append("Vinagre")
#lista_de_compras = ["Leite", "Macarrão", "Ovo", "Farofa", "Japonês", "Peixe", "Carne", "Frango", "Vinagre"] <- lista atual

print("Vinagre adicionado")
print(lista_de_compras)

# Insert
lista_de_compras.insert(1, "Suco de laranja")

print("Suco de laranja adicionado na posição 1")
print(lista_de_compras)

# extend (merge)
lista_impar = [1, 3, 5, 7, 9]
lista_par = [2, 4, 6, 8]

print(lista_impar)
print(lista_par)

lista_par.extend(lista_impar)

print(lista_par)

# Como remover

# Remover especificando o elemento
lista_de_compras.remove("Vinagre")

lista_impar.remove(1)


print(lista_impar)


# Remover especificando o índice
lista_construtor_davy.pop()
print(lista_de_compras) # Suco de laranja indice 01
lista_de_compras.pop(1) # Remove ele
print(lista_de_compras)
lista_construtor_fs.pop(3)
lista_construtor_fs.remove("Livre")

print(lista_construtor_fs)

# Exclusão da estrutura/índice
#del lista_de_compras[1] # Remove um indice especificado

#del lista_de_compras # deleta a estrutura toda

#print(lista_de_compras)

# Loop pelas estruturas

# Apenas o elemento
for item in lista_de_compras:
    print(f"Exibindo o elemento: {item}")

# Elemento + índice
for indice, item in enumerate(lista_de_compras, start=1):
    print(f"{indice}º item: {item}")