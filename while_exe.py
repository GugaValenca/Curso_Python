while True:

    numero = input("Digite um número: ")

    if not numero.isdigit():
        print("Entrada inválida! Digite apenas números.")
    else:
        numero = int(numero)

        if numero < 0:
            print("Número inválido, digite apenas números positivos.")
        else:
            # Executa a contagem regressiva até 0
            while numero >= 0:
                print(numero)
                numero -= 1  # Decrementa o número em 1 a cada iteração

print("Fim da contagem")