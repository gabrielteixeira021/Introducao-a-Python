## Exercicio 01 - Lista de Compras
# Crie uma lista com 5 itens de compras e exiba cada item com sua posição na lista.

lista_de_compras = ["arroz", "feijão", "leite", "pão", "macarrão"]

for idx, item in enumerate(lista_de_compras, start=1):
    print(f"{idx}º item: {item}")
