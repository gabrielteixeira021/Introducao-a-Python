"""
QUESTÃO 01: Faça um programa que leia um 
número  inteiro  positivo  N e  exiba  todos  os múltiplos de Y inferiores a N, onde N e Y são 
fornecidos pelo usuário.
"""

N = int(input()) # 10
Y = int(input()) # 2

i = Y 
# percorre o intervalo de Y a N 
while i < N:
    
    # Verificar se é multiplo
    if i % Y == 0:
        print(Y) # 2, 4, 6, 8 
        print("É múltiplo: ")
    i+=1