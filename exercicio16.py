nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
 
media = (nota1 + nota2 + nota3) / 3

print(f"media: {media: .2f}")

if media >= 7:
    print("aluno aprovado")
elif media >= 5:
    print ("aluno em recuperação")
else:
    print("aluno reprovado")