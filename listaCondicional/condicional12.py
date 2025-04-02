n1 = float(input("Digite um numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

if(n1>n2 and n2>n3):
    print("Ordem decrescente")

elif (n1<n2 and n2<n3):
    print("Ordem crescente")

else:
    print("Numeros sem ordem")


