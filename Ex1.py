# Ex1 informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
 

entrada = input("Digite um número: ")

if entrada.isdigit():
    numero = int(entrada)
    resultado = "par" if numero % 2 == 0 else "ímpar"
    print(f"O número {numero} é {resultado}.")
else:
    print("Você não digitou um número inteiro.")   


   

