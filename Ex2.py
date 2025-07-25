# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora = int(input("Digite a hora (0-23): "))
if 0 <= hora <= 23:
    if hora < 12:
        print("Bom dia!")
    elif hora < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
else:
    print("Hora inválida.")