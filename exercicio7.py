num1 = int(input("insira o primeiro numero que deseja: "))
num2 = int(input("insira o segundo numero que deseja: "))
escolha =input ("insira a operação que deseja: (adicao, subtracao, multiplicacao e divisao)")
adicao= num1+num2
subtracao= num1-num2
multiplicacao= num1*num2
divisao= num1/num2
if escolha=="adicao":
   print(adicao)
elif escolha=="subtracao":
   print(subtracao)
elif escolha=="multiplicacao":
   print(multiplicacao)
elif escolha=="divisao":
    print(divisao)
else :
    print("Operação não existe.")