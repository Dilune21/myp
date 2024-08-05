# Tabuada Númerica
def mostrar_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
        mostrar_tabuada(numero)
    except ValueError:
        print("Digite um número inteiro válido.")

if __name__ == "_main_":
    main()