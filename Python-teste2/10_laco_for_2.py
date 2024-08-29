print ("====LOJAS====")
print ("  ")

lojas = ["Santo André", "São Bernardo", "São caetano", "Diadema"]

for i, loja in enumerate(lojas, 1):
    print(f"(i) - {loja}")
    print ("  ")

    loja_selecionada = int(input("Selecione a loja desejada: "))

    if 1 <= loja_selecionada <= len(lojas):
        print(lojas[loja_selecionada -1])
    else:
        print("Loja inválida")