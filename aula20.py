primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

print("Você digitou os valores:", primeiro_valor, "e", segundo_valor)

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior que {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor=} é maior que {primeiro_valor=}")
else:
    print("Os dois valores são iguais")

    