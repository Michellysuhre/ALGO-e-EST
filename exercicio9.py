temperatura=int(input("insira a temperatura"))
if temperatura <20:
    print("sua temperatura esta fria")
elif temperatura >20 and temperatura <26:
    print("sua temperatura esta morna")
elif temperatura > 27:
    print("sua temperatura esta quente")
else:
    print("deu errado")
