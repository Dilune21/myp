# Esse é um comentário !

Local = input("Qual foi o local que você viajou?")
match Local:
    case "Disney"
        print("Local execelente para levar as crianças! ")
    case "Paris"
        print("Local perfeito para passeios romanticos! ")
    case :
        print(" Não conheço esse lugar...")