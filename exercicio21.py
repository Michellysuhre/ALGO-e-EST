numeros = [int(input("Digite um número: ")) for _ in range(10)]

for numero in numeros:
    print(numero)

soma = 0
for numero in numeros:
    soma += numero
print("Soma dos números: ", soma)
