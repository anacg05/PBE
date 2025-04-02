idade =int(input("Digite uma idade:"))

if (idade <16):
    print("Não vota")

elif (idade>=18 and idade<70):
    print("Voto obrigatório")

else:
    print("Voto Facultativo")
