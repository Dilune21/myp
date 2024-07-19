# Jogo de futebol
posisão = input("Digite a posisão do jogador: ")

if posisão == "goleiro" or posisão == "zalgueiro" or posisão == "lateral":
    print("Defesa!")
elif posisão == "volante" or posisão == "meia":
    print("meio-campo!")
elif posisão == "ponta" or posisão == "atacante" or posisão == "centroavante":
    print("Ataque!")
else:
    print("Teimoso!")