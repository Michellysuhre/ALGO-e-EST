numeros = []
pares = []
impares = []

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número: "))
numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
else:
    impares.append(numero)

print("A quantidade de números pares é: ", pares)
print("A quantidade de números impares é :", impares)