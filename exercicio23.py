
numero = int(input("Digite o número desejado para ver a tabuada: "))
tabuada = []

for i in range(1, 11):
    tabuada.append(numero * i)

print("Tabuada do", numero , "é: ")
for valor in tabuada:
    print(valor)