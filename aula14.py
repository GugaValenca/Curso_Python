a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'a={}, b={}, c={:.2f}'
# 
formato = string.format(a, b, c) # (a, b, c) são argumentos posicionais do método format
# (nome1=a, nome2=b, nome3=c) são argumentos nomeados do método format

print(formato)