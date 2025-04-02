import math

print("16 - Esse programa calcula a raiz quadrada de um número")
num = float(input("Insira um número: "))

if num < 0:
    resultado = "Não é possível calcular a raiz quadrada de um número negativo."

elif num > 100:
    resultado = "Número muito grande, reduza para um valor abaixo de 100."

else:
    raiz = num ** 0.5
    resultado = f"A raiz quadrada de {num} é aproximadamente {raiz:.2f}."

print(resultado)
