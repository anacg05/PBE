grau = float(input("Digite os graus em celsius: "))

if(grau<10):
    print("Frio")

elif(grau>=10 and grau<25):
    print("Aconchegante")

elif(grau>=25 and grau<40):
    print("Quente")

else:
    print("Muito quente")