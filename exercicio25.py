
segredo = int(input("Digite o número secreto (entre 1 e 20): "))
palpites = []
acertou = False

for tentativa in range(10):
    palpite = int(input("Tente adivinhar o número: "))
palpites.append(palpite)

if palpite == segredo:
    acertou = True

if acertou:
    print("Você acertou!")
else:
    print("Você não acertou o número.")

print("Palpites feitos:", palpites)