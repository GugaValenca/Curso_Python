# Precedência de operadores em Python
# A ordem de precedência dos operadores em Python é a seguinte:
# 1. (n + n)-- primeiro será executado o q estiver entre parenteses.
# 2. ** -- Potenciação/Exponenciação
# 3. * / // % -- Multiplicação, Divisão, Divisão inteira e Módulo (resto da divisão)
# 4. + - -- Adição e Subtração
conta_1 = (1 + 1) ** (5 + 5) # 1024
conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024
print(conta_1)
print(conta_2)