# Demostrção de operadores logicos em condicionais...
print("o que voce vai fazer amanha de manha?")
print("dormir/estudar/planejar")
manha = input()
print("oque voce vai fazer amanha de tarde?")
print("jogar / treinar / trabalhar")
tarde = input()

if not manha or not tarde:
    print("voce precisa dizer o que voce vai fazer!")
else:
    if manha == "dormir" or tarde =="jogar":
    print("voce esta disperdicao o seu dia!")
elif manha =="estudar" or tarde =="treinar":
    print("que bom voce ira se aprefeiçoar!")
elif manha =="planejar" and tarde == "trabalhar":
    print