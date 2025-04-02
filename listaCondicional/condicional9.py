valor = float(input("Informe o valor total:"))

if (valor <100):
    print("5% de desconto")

elif (valor>=100 and valor<500):
    print("10% de desconto")

else:
    print("15% de desconto")