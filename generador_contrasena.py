import random
import string


def generar_contrasena():
    #Asi optenemos las letras completas en mayuscula y minuscula
    letras = list(string.ascii_letters)
    #lista de los simbolos especiales.
    simbolos = list(string.punctuation)
    #lista de numeros
    numeros = list(string.digits)

    caracteres = letras + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres) #Con la funcion choice elijo un caracter al azar.
        contrasena.append(caracter_random)


    contrasena = "".join(contrasena)#Con este metodo se convierte una lista a caracteres
    return contrasena


def run():
    contrasena= generar_contrasena()
    print('Tu nueva contraeña es: ' + contrasena)
    
    


if __name__=='__main__':
    run()