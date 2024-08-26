def registrar_usuario (lista_usuarios, lista_contrasenas):
    usuario = input("Ingrese un nombre de usuario: ")
    # VERIFICA SI EL NOMBRE DE USUARIO YA EXISTE
    while usuario in lista_usuarios:
        print("Ese usuario ya existe")
        usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese la contrasena del usuario: ")
    verificar_contrasena = input("Volvé a ingresar la contrasena : ")
    # VERIFICA QUE LAS CONTRASEÑAS COINCIDAN
    while contrasena == verificar_contrasena:
        print("Error. Las contraseñas no coinciden, intente de nuevo. ")
        contrasena = input("Ingrese la contrasena del usuario: ")
        verificar_contrasena = input("Volvé a ingresar la contrasena : ")
    print("Listo ", usuario, "!")
    # SE GUARDAN EN LISTAS EL USUARIO Y LA CONTRASEÑA
    usuario.append(lista_usuarios)
    contrasena.append(lista_contrasenas)
