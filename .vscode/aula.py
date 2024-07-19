# Correção de exercicios...
nota1 =int(input("digite a nota1:"))
nota2 =int(input("digite a nota2:"))
nota3 =int(input("digite a nota3"))
nota4 =int(input("digite a nota4"))
Média = (nota1 + nota2 + nota3 +nota4) / 4

if Média >=6:
  print("você esta aprovado!")
elif Média < 4 :
  print("você está reprovado...")
elif 4 <= Média <6:
  print("Recuperação...")

print(f"Sua média é {Média}.")
print(type(Média))