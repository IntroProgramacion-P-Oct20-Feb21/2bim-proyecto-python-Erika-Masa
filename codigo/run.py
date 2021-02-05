"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""

def crearFacebook():
    """
         explicación de método
     """
    print("Creando cuenta de Facebook")
    usuario = input("ingrese el nombre del usuario:\n ")
    edad = int (input("ingrese su edad:\n"))
    ciudad = input("ingrese el nombre de su ciudad: \n")
    pais = input("ingrese el nombre de su pais:\n ")
    correo = input("ingrese su correo electronico\n")
    cadena = "facebook \t \n El nombre del usuario es: %s, su edad es:%d," \
             "habitat en la ciudad de: \n %s En el pais de : \n %s, su correo electroni es :\n %s"
    (usuario,edad,ciudad,pais,correo)
    return cadena

def crearTwitter():

    print("usted creara una cuenta twitter")
    usuario = input ("ingrese el nombre del usuario")
    nombre = input("Ingrese sus nombres")
    apellidos= input("Ingrese sus apellidos")
    edad=int(input("Ingrese su edad"))
    ciudad = input("Ingrese el nombre de su ciudad")
    pais = input("Ingrese el nombre de su pais")
    idioma = input("Ingtese su idioma")
    correo = input ("Ingrese su correo")

    print("Twitter\n \t El nombre del usuario es: %s, sus nombres son: %s, sus apellidos son: %s" \
          "tiene una edad de: %d, vive en la ciudad de: %s, en el país: %s, su idioma es: %s" \
          "su correo eletrónico es: %s" % (usuario, nombre, apellidos, edad, ciudad, idioma, pais, correo))


def crearWhatsapp():
    nombre = input("Ingrese el nombre de usuario")
    numero = int(input("Ingrese su numero de telefono"))
    edad=int(input("Ingrese su edad"))
    ciudad= input("Ingrese el nombre de su ciudad")
    pais=input("ingrese el nombre de su pais")
    cadena = "Whatsapp\n \t El nombre del usuario es: %s, su número de celular es: %d, tiene una edad de: %d, vive en la ciudad de: %s," \
               "en país de: %s" % (nombre, numero, edad, ciudad,pais)
    return cadena

def crearTelegram ():
    def crearTelegram():
        usuario = input("Ingrese el nombre de usuario: ")
        numero = int(input("Ingrese su número de celular: "))
        ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
        pais = input("Ingrese el país en el que vive: ")
        interes = input("Ingrese su área de interes: ")
        print(" Telegram \n \t El nombre del usuario es: %s, su número de celular es: %d, vive en la ciudad de: %s," \
              "en país de: %s y su interés peronal es: %s" % (usuario, numero, ciudad, pais, interes))

def crearsignal ():
    usuario = input("Ingrese el nombre de usuario: ")
    numero = int(input("Ingrese su número de celular: "))
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    pais = input("Ingrese el país en el que vive: ")
    hobby = input("Ingrese su hobby favorito")
    cadena = "\tSignal\nUsuario: %s\nNumero de telefono: %d\nCiudad: %s\n"\
    "Pais: %s\nHobby favorito: %s\n"%(usuario, numero, ciudad, pais, hobby)
    return cadena

def crearInstagram ():
    usuario = input("Ingrese el nombre de usuario: ")
    ciudad = input("Ingrese el nombre de la ciudad en la que vive: ")
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese su correo electrónico: ")
    print("\tInstagram\nUsuario: %s\nCiudad: %s\nEdad: %d\n"\
    "Correo: %s\n"%(usuario, ciudad, edad, correo))

def crearFlickr ():
    usuario = input("Ingrese el nombre de usuario: ")
    correo = input("Ingrese su correo electrónico: ")
    cadena = "\tFlickr\nUsuario: %s\nCorreo: %s\n" %(usuario, correo)
    return cadena

def obtenerMensaje(contador):
    mensajeFinal = ["Campaña con poca afluencia",
    "Campaña moderada siga adelante", "Excelente campaña"]
    if ((contador >= 1) and (contador <=5)):
        cadenaFinal = mensajeFinal[0]
    if ((contador >= 6) and (contador <= 15)):
        cadenaFinal = mensajeFinal[1]
    else:
        if ((contador >= 16)):
            cadenaFinal = mensajeFinal[2]
    return cadenaFinal




def principal():
    bandera = True
    contadorCuentas = 0
    while (bandera):
        opcion1 = int(input("Ingresar 1 para crear una cuenta en Facebook\n"\
        f"Ingresar 2 para crear una cuenta de Twitter:\n"\
        f"Ingresar 3 para crear una cuenta en Whatsapp:\n"\
        f"Ingresar 4 para crear una cuenta en Telegram:\n"\
        f"Ingresar 5 para crear una cuenta en Signal:\n"\
        f"Ingresar 6 para crear una cuenta en Instagram:\n"\
        f"Ingresar 7 para crear una cuenta en Flickr: \n "))
        if opcion1 == 1:
            cuenta_Facebook=crearFacebook()
            print(cuenta_Facebook)
        else:
            if opcion1 == 2:
                crearTwitter()
            else:
                if opcion1 == 3:
                    cuenta_Whatsapp = crearWhatsapp()
                    print(cuenta_Whatsapp)
                else:
                    if opcion1 == 4:
                        crearTelegram()
                    else:
                        if opcion1 == 5:
                            cuenta_signal = crearsignal()
                            print(cuenta_signal)
                        else:
                            if opcion1 == 6:
                                crearInstagram()
                            else:
                                if opcion1 == 7:
                                    cuenta_Flickr = crearFlickr()
                                    print(cuenta_Flickr)
        if ((opcion1 >= 1) & (opcion1 <= 7)):
            contador = contador + 1
        else:
            print("Error, intente colocar los número presentados \n")


        opcion2 = input("Escriba SI para crear mas cuentas\n Escribir no para dejar de crear cuentas ")
        opcion2 = opcion2.lower()
        if (opcion2 == "no"):
            bandera = False
            print(obtenerMensaje(contadorCuentas))




# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
if __name__ == "__main__":
    principal()

