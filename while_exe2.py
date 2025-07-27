
soma = 0

while True:
    numero = input('Digite um número: ')

    if not numero.isdigit():
        print('Entrada inválida! Digite apenas números.')
        continue
    numero = int(numero)

    if numero % 2 == 0:
        soma += numero
    else:
        print('A soma dos números pares é:', soma)
        break