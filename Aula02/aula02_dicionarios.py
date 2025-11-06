# Dicionarios


# Como Inicializar 

contato_gabriel = {"nome": "Gabriel", "sobrenome": "Teixeira", "telefone": "99999-9999", "idade": 20}
contato_markolas = {"nome:" "Markolas", "sobrenome", "telefone:" "2196922-5544", "idade:" "13"}
contato_davy = {"Nome": "Davy", "Sobrenome": "Andrade", "Telefone": "2191234-5678", "Email": "example@email.com"}
contato_noct = {"Nome": "Tenet", "Sobrenome": "Noctis", "Telefone": "None", "Email": "None", "Endereço": "Fim do Tempo"}

# Como inicializar estruturas de dados em dicionarios
lista_de_contatos = {
    "Nome": [
             "Gabriel (Gadão Guerreiro)", 
             "Marcos (Japonegro)", 
             "Davy (Ursao)", 
             "Fellype (Enciclopédia)", 
             "Carlos (onlyfans)"
             ],
      "Telefone": [
        "21 54682135",  
        "21 9794-2131",
        "87 6523451"
      ],   
      
      "Email": [
          "gadaoguerreiro@gmail.com",
          "japonegro@gmail.com",
          "theursao@gmail.com",
          "chatgpt@gmail.com",
          "onlyfans@gmail.com",
      ],
      
      "Endereço": [
          "Casa da Soso",
          "Casa da Soso",
          "Casa da Mine Dele",
          "Fim dos Tempos",
          "Inicio dos Tempos"
      ]
}

# Como acessar / visualizar

# Como visualizar as chaves do dicionario
print(lista_de_contatos.keys())


# Acessando um dicionario simples (chave-valor unitario)
nomes = contato_gabriel["nome"]
print(nomes)

# Acesso a um dicionario complexo (chave-valor(estrutura de dados))
lista_nomes = lista_de_contatos["Nome"]
print(lista_nomes)

lista_emails = lista_de_contatos["Email"]
print(lista_emails)

lista_telefones = lista_de_contatos["Telefone"]
print(lista_telefones)


# Como alterar o valor

# Alteração direta
contato_gabriel["telefone"] = "932193129"
print(contato_gabriel)

contato_davy["Telefone"] = "40028922"
print(contato_davy)

# Alteração por método
contato_gabriel.update({"telefone": "3212345"})
print(contato_gabriel)

contato_davy.update({"Telefone": "08006969"})
print(contato_davy)

contato_noct.update({"telefone": "999999"})

contato_markolas.update({"telefone": "54654351"})

# Como adicionar



# Como remover



# Como iterar