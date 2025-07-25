
entrada = input("Digite um número: ")

if entrada.isdigit():
    numero = int(entrada)
    resultado = "par" if numero % 2 == 0 else "ímpar"
    print(f"O número {numero} é {resultado}.")
else:
    print("Você não digitou um número inteiro.")   


   

