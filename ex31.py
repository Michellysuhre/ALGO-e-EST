numero = int(input("adicione a tabuada que deseja realizar: "))


def tabuada(numero):
    print(f'tabuada do {numero}:')
    for i in range(1,11):
          print(f'{numero} x {i} ={numero *i }')

tabuada(numero)