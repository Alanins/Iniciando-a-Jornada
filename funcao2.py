#Microatividade 6: Descrever a utilização argumentos defunções no Python

def loginUsuario(perfil):
    if perfil.lower()=="admin":
        print("Bem-vindo. Administrador")
    else:
        print("Bem-vindo. Usuario")

loginUsuario("Admin")
loginUsuario("user")