nomecerto = "admin"
senhacerta = "1234"

nomeusuario = input("insira um nome de usuario: ")
senha = input("insira sua senha: ")
if nomeusuario == nomecerto and senha == senhacerta:
    print("seja bem-vindo!")
else:
    print("acesso negado!")
