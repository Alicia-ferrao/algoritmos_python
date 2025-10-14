massa = float(input("Digite o seu peso (kg) : "))
altura = float(input("Digite a sua altura em (m) : "))

imc = massa/altura ** 2

print(f"O Imc é de : {imc:.2f}")


if imc < 18:
    print("Muito abaixo do peso")
elif imc >= 18 and imc < 20:
    print("abaixo do peso")
elif imc >= 20 and imc < 25:
    print("Peso ideal")
else:
    print("Sobrepeso")
