cpf = input("Digite o número do CPF (XXX.XXX.XXX-XX): ").replace(".", "").replace("-", "")

if not cpf.isdigit() or len(cpf) != 11:
    print("CPF inválido")
else:
    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    soma1 = (int(cpf[0]) * peso1[0] + int(cpf[1]) * peso1[1] + int(cpf[2]) * peso1[2] +
             int(cpf[3]) * peso1[3] + int(cpf[4]) * peso1[4] + int(cpf[5]) * peso1[5] +
             int(cpf[6]) * peso1[6] + int(cpf[7]) * peso1[7] + int(cpf[8]) * peso1[8])
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = (int(cpf[0]) * peso2[0] + int(cpf[1]) * peso2[1] + int(cpf[2]) * peso2[2] +
             int(cpf[3]) * peso2[3] + int(cpf[4]) * peso2[4] + int(cpf[5]) * peso2[5] +
             int(cpf[6]) * peso2[6] + int(cpf[7]) * peso2[7] + int(cpf[8]) * peso2[8] +
             int(cpf[9]) * peso2[9])
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        print("CPF Válido")
    else:
        print("CPF Inválido")
