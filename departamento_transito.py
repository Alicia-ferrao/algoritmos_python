print("----------------------------")
print("--DEPARTAMENTO DE TRANSITO--")
print("----------------------------")
ano_atual = int(input("Ano Atual (yyyy) : "))
ano_nasc = int(input("Ano Nascimento (yyyy) : "))
idade   = ano_atual- ano_nasc
print("------Status------")
print(f"Idade {idade}")
if idade >= 18 :
    print("Apto para tirar a carta")
else:
    print("Não Apto para tirar a carta")
print("----------------------------")