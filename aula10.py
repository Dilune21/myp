# Solicita os três números distintos do usuário
x = float(input("Digite o primeiro número (X): "))
y = float(input("Digite o segundo número (Y): "))
z = float(input("Digite o terceiro número (Z): "))

# Verifica se os números estão em ordem crescente
if x < y < z:
    print("Os números estão em ordem crescente.")
# Verifica se os números estão em ordem decrescente
elif x > y > z:
    print("Os números estão em ordem decrescente.")
# Caso contrário, os números estão misturados
else:
    print("Eles estão misturados!")