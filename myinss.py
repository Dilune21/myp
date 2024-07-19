# Solicita as informações do trabalhador
sexo = input("Digite o seu sexo (masculino/feminino): ").lower()
idade = int(input("Digite a sua idade: "))
tempo_contribuicao = int(input("Digite o seu tempo de contribuição (em anos): "))
insalubridade = input("Trabalhou em ambiente insalubre? (sim/não): ").lower()

# Define os requisitos para aposentadoria
idade_minima_homem = 65
idade_minima_mulher = 60
tempo_contribuicao_minimo = 35

# Aumenta a idade mínima em 20% se houve exposição à insalubridade
if insalubridade == "sim":
    idade_minima_homem = int(idade_minima_homem * 1.2)
    idade_minima_mulher = int(idade_minima_mulher * 1.2)

# Verifica se o trabalhador está apto para se aposentar
if sexo == "masculino":
    if idade >= idade_minima_homem and tempo_contribuicao >= tempo_contribuicao_minimo:
        print("Você está apto para se aposentar.")
    else:
        print("Você não está apto para se aposentar.")
elif sexo == "feminino":
    if idade >= idade_minima_mulher and tempo_contribuicao >= tempo_contribuicao_minimo:
        print("Você está apto para se aposentar.")
    else:
        print("Você não está apto para se aposentar.")
else:
    print("Sexo inválido. Por favor, digite 'masculino' ou 'feminino'.")