nome = input("Digite seu nome: ").strip()

if not nome or not nome.isalpha():
     print("Você não digitou um nome!")
elif len(nome) <= 4:
     print(f"Seu nome é curto!")
elif len(nome) <= 6:
     print(f"Seu nome é normal!")
else:
     print(f"Seu nome é muito grande!")
