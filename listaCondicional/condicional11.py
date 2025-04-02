peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros e com  ponto: "))
imc = peso / (altura ** 2)

print("Seu IMC é: {:.2f}".format(imc))

if(imc<18.5):
    print("Está abaixo do peso.")

elif(imc>=18.5 and imc<=24.9):
    print("O peso está normal.")

elif(imc>=25 and imc<=29.9):
    print("Está com sobrepeso.")

else:
    print("Está com obesidade.")