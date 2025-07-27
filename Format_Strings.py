#Formatação de strings

preco = 1234.567
print(f"Preço normal: {preco}")
print(f"Preço formatado: {preco:.2f}")       # duas casas decimais
print(f"Preço com vírgula: {preco:,.2f}")   # separador de milhar


import locale

# Define a localização para Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor = 1234567.89

# Usa a formatação de moeda padrão do Brasil
print(f"Valor formatado no padrão brasileiro: {locale.currency(valor, grouping=True)}")
# Exibe o valor formatado com separador de milhar e símbolo de moeda


# Formatação de data e hora
from datetime import datetime

hoje = datetime.now()
print(f"Hoje é {hoje:%d/%m/%Y}")
print(f"Agora é {hoje:%H:%M:%S}")


# Exemplo de formatação condicional

idade = 20
print(f"Maior de idade? {'Sim' if idade >= 18 else 'Não'}")
