nomes = []

# Coleta os nomes
for i in range(5):
    nome = input("Digite o nome de um amigo: ")
nomes.append(nome)

# Ordenação manual sem usar temp
for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        if nomes[i] > nomes[j]:
            nomes[i], nomes[j] = nomes[j], nomes[i] # troca direta

# Exibe os nomes em ordem alfabética
print("Nomes em ordem alfabética:")
for nome in nomes:
    print(nome)