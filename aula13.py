nome = 'Gustavo Valenca'
altura = 1.80
peso = 86.5
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
# :,.2f = arredonda para 2 casas decimais e acrescenta uma virgula.
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Gustavo Valenca tem 1.80 de altura,
# pesa 86.5 quilos e seu IMC é
# 26.697530864197528