palavras = [input("Digite uma palavra: ") for _ in range(6)]

contagem = 0
for palavra in palavras:
    if len(palavra) > 5:
        contagem += 1

print("Palavras com mais de 5 caracteres:", contagem)
