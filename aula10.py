# Solicita os três números distintos do usuário
x = int(input("Digite o primeiro número x:"))
y = int(input("Digite o segundo número Y:"))
z = int(input("Digite o terceiro número Z:"))

if x < y and y < z:
    print("Os números estão em ordem crescente.")
elif x > y and y > z:
    print("Os números estão em ordem decrescente.")

else:
    print("Eles estão misturados!")