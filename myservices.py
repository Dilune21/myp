# Solicita se o serviço foi prestado
servico_prestado = input("O serviço foi prestado atendendo a todos os requisitos? (sim/não): ").lower()

# Verifica se o serviço foi prestado
if servico_prestado == "sim":
    # Solicita a avaliação do serviço
    nota = int(input("Avalie o serviço prestado (1-5): "))
    
    # Verifica a nota e exibe a mensagem correspondente
    if nota == 1:
        print("Péssimo")
    elif nota == 2:
        print("Ruim")
    elif nota == 3:
        print("Razoável")
    elif nota == 4:
        print("Bom")
    elif nota == 5:
        print("Ótimo")
    else:
        print("Nota inválida")
else:
    # Solicita a reclamação do usuário
    print("Por favor, relate as suas reclamações.")