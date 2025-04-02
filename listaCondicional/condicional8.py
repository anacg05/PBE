n1 = float(input("Informe um comprimento:"))
n2 = float(input("Informe o segundo comprimento:"))
n3 = float(input("Informe o terceiro comprimento:"))

if (n1 + n2 < n3) or (n1 + n3 < n2) or (n2 + n3 < n1):
    print("Nao é um triângulo")

elif (n1 == n2) and (n1 == n3) :
    print("Equilátero")

elif (n1==n2) or (n1==n3) or (n2==n3):
    print("Isósceles")

else:
        print("Escaleno")

