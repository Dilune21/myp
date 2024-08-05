def perguntar_melhor_clube():
    melhor_clube = "Flamengo"  # Defina o melhor clube aqui
    while True:
        resposta = input("Qual é o melhor clube de futebol do Brasil? ")
        if resposta.strip().lower() == melhor_clube.lower():
            print("Parabéns! Você acertou!")
            break
        else:
            print("Resposta errada. Tente novamente.")

if __name__ == "_main_":
    perguntar_melhor_clube()