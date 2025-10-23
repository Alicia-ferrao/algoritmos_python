print("-----------------------------")
print("      SPORTING X BENFICA     ")
print("-----------------------------")

# Leitura dos gols
equipa1 = int(input("Quantos golos do Sporting: "))
equipa2 = int(input("Quantos golos do Benfica: "))

print("-----------------------------")

# Calcula a diferença absoluta de gols
diferenca = abs(equipa1 - equipa2)
print("DIFERENÇA:", diferenca)

# Verifica o status do jogo com if/elif/else
if diferenca == 0:
    print("STATUS: EMPATE")
elif diferenca in [1, 2, 3, 4]:
    print("STATUS: PARTIDA NORMAL")
else:
    print("STATUS: GOLEADA")

print("-----------------------------")