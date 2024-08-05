import time

def contagem_regressiva():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)  # Espera 1 segundo antes de continuar a contagem
    print("Feliz Ano Novo!")

if __name__ == "_main_":
    contagem_regressiva()