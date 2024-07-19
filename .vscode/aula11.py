# Atividade 2
nome_time = input("Digite o nome do time:")
posição = int(input("Digite a posição do time na tabela de classificação:"))

#Verifica a classificação do time com base na posição
if posição == 1:
    classificação ="Campeão"
elif 2 <= posição <= 4:
    classificação = "Libertadores"
elif 5 <= posição <=12:
    classificação = "Sul-Americana"
elif 13 <= posição <= 16:
    classificação = "Nada"
elif 17 <= posição <= 20:
    classificação = "Rebaixado"
else:
    print("posição invalida")

# Exibe a classificação do time
print(f"O Time {nome_time} está classificado como: {classificação}")