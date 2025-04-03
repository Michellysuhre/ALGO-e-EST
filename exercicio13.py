nome = input("insira seu nome: ")
idade = int(input("insira sua idade: "))
turma = int(input("insira sua turma: "))
 
nomeins = nome
idadeins = idade
turmains = turma 

print(f("Aluno cadastrado com sucesso: {nome}, {idade} anos, turma {turma}"))

if idade >= 6:
    print("matrícula válida")
else:
    print("matrícula inválida")
    