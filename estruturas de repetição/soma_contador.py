contador= 1
soma = 0

while contador <=3:
    num = int(input(("Digite o {}º numero : " .format(contador))))
    soma = soma + num
    contador =contador +1

print(f"A soma de todos os numero foi {soma}")
