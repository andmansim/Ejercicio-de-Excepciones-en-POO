import re

class UsIncorrecto(BaseException):
    pass
class DiFormato(BaseException):
    pass
class AtaqueBloq(BaseException):
    pass

def intento(contador1):
    usuario = input()
    validacion = re.search("@", usuario) #si no está nos devuelve None
    print(contador1)
    print(validacion)

    if validacion != None and contador1 > 0:
        try:
            usuario == "vicente@eni.es"
            print("¡Bienvenido Vicente!")
            
            
        except DiFormato:
            contador1 = contador1 - 1
            print(contador1)
            print("La dirección de correo tiene que tener la forma de xxx@xx.xx")

    if validacion == None and contador1 > 1:
        contador1 = contador1 - 1
        print(contador1)
        UsIncorrecto
        print("Usuario incorrecto, introduce tu dirección de correo")
            
    if contador1 == 1 and validacion == None:
        AtaqueBloq
        print("Por motivos de seguridad, su usuario se ha bloqueado")
            

contador = 3
print("Hola Vicente, por favor introduce tu correo electrónico para acceder")
intento(contador)

