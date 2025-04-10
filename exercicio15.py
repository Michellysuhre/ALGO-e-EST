nome = input(" adicione aqui o nome do produto: ")
quant = int(input("adicione a quantidade do produto desejado: "))
precouni = float(input("adicione o preço unitario: "))

total = quant*precouni
desconto5 = total*0,5
if total >= 100:
    print("seu desconto é de: {desconto5} ")
    
    
