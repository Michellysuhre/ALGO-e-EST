valor_compra=float(input("insira o valor da compra "))
if valor_compra >= 100:
    prec_desc = valor_compra*0.9
    print("o valor do desconto é :", prec_desc)
else:
    print("valor da compra sem desconto: ",valor_compra)

