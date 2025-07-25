nome = input("Digite seu nome: ")

if len(nome) <= 4:
     print(f"Seu nome é curto!")
elif 5 <= len(nome) <= 6:
     print(f"Seu nome é normal!")
elif len(nome) > 6:
     print(f"Seu nome é muito grande!")
else:
     print("Nome inválido!")