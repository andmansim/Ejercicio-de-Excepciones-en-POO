import re

class UsIncorrecto(BaseException): #le indicamos que utilizamos esta clase 
    pass
class DiFormato(BaseException):
    pass
class AtaqueBloq(BaseException):
    pass


def errores(usuario, contador1): # valida si el correo es correcto y recoge cada error
    validacion = re.search("@", usuario) #si no está nos devuelve None
    if usuario == "vicente@eni.es":
        print("Bienvenido, Vicente")
    elif contador1 == 1:
        raise AtaqueBloq
    elif validacion == None:
        raise UsIncorrecto #nos manda al except con esta etiqueta
    elif  usuario != "vicente@eni.es":
        raise DiFormato

    
def intento(contador1):
    if contador1 > 0:
        try:
            usuario = input()
            errores(usuario, contador1)           
        except UsIncorrecto:
            contador1 = contador1 - 1
            print("Usuario incorrecto, introduce tu dirección de correo")
            intento(contador1)
        except DiFormato:  
            contador1 = contador1 - 1
            print("La dirección de correo tiene que tener la forma de xxx@xx.xx")
            intento(contador1)
 
        except AtaqueBloq:
            print("Por motivos de seguridad, su usuario se ha bloqueado")
            


