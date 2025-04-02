data = input("Escreva a data no seguinte formato (dd/mm/aaaa): ")
partes = data.split("/")
dia = int(partes[0])
mes = int(partes[1])
ano = int(partes[2])

if mes<1 or mes>12:
    print("O mês deve estar entre 1 e 12.")
else:
    if mes==2:
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            limite = 29
        else:
            limite = 28
    elif mes in [4, 6, 9, 11]:
        limite = 30
    else:
        limite = 31

    if dia<1 or dia>limite:
        print(f"O mês {mes} no ano {ano} tem no máximo {limite} dias.")
    else:
        print(f"{ano:04d}-{mes:02d}-{dia:02d}")
