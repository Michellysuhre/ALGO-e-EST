email_certo = (input("insira um e-mail"))
email_certo=str.lower(email_certo)

senha= (input("faça uma senha "))
if len(senha) < 8:
    print("senha pequena demais")
else:
    senha_certa=senha
    email=input("insira o email:")
    senha=input("insira o senha:")
    if email==email_certo:
        if senha== senha_certa:
            print("bem-vindo")
    else:
        print("email ou senha incorretos")