# nome = (input ('Qual o seu nome? '))
# sobrenome = (input ('Qual o seu sobrenome? '))

# print (f'Olá, {nome} {sobrenome}!')

# Exemplo 1
# numero_1 = int (input ('Digite um número: '))
# numero_2 = int (input ('Digite outro número: '))

# print (f'A soma dos números é {numero_1 + numero_2}')

# Exemplo 2

numero_1 = input ('Digite um número: ')
numero_2 = input ('Digite outro número: ')

# int_numero_1 = int (numero_1)
# int_numero_2 = int (numero_2)

# print (f'A soma dos números é {int_numero_1 + int_numero_2}')

if numero_1.isdigit() and numero_2.isdigit():
    print (f'A soma dos números é {int(numero_1) + int(numero_2)}')
else:
    print ('Você não digitou números válidos.')




