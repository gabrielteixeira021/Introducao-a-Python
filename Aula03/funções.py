# Aula 03 - Funções

# Entrada -> F(x) -> Saída


def greetings(texto):
    return texto + "Bom dia"


""" 
Ex01: Crie uma função que contenha entrada e saída
"""

numero = int(input("Insira o valor de x: "))

def negativa(x):
    
    if x < 0:
        return True
    else: 
        return False

print(f"Resultado Função: {negativa(numero)}")


"""

entrada -> f(x) -> saida

entrada = 2


f(x)


f(entrada)

x = numero

"""

"""
Ex02: Crie uma função que receba obrigatóriamente dois valores inteiros A e B, e retorne A+B. 
"""

a = int(input("Valor A: "))
b = int(input("Valor B: "))

def soma(a: int, b: int): 
    
    adicao = a + b

    return adicao

print(f"Soma dos valores é: {soma(a, b)}")


"""
Ex03: Implemente uma função que receba três valores (A, B, C) e retorne D, sendo D = (B * B) - 4 * A * C.
"""

