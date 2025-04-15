
numeros = [int(input("Digite um número: ")) for _ in range(5)]

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
if numero < menor:
    menor = numero

print("Maior número:", maior)
print("Menor número:", menor)