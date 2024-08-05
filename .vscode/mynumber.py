# Demostração do uso de estutura repetitiva...
NUMERO = 1
while NUMERO >= 0:
    print("Digite um número negativo para sair:")
    NUMERO = int(input())
    break
    print("Esse texto não será exibido! Mas...")
else:
    print("O número digitado foi:", NUMERO)