import random

# Função para determinar o vencedor
def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

# Lista de escolhas possíveis
escolhas = ["pedra", "papel", "tesoura"]

# Solicita a escolha do jogador
jogador = input("Escolha pedra, papel ou tesoura: ").lower()

# Escolha aleatória do computador
computador = random.choice(escolhas)

# Exibe as escolhas
print(f"Você escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

# Determina e exibe o resultado
resultado = determinar_vencedor(jogador, computador)
print(resultado)