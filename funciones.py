import re

class UsIncorrecto(BaseException): #le indicamos que utilizamos esta clase 
    pass
class DiFormato(BaseException):
    pass
class AtaqueBloq(BaseException):
    pass


def errores(usuario): # valida si el correo es correcto y recoge cada error
    validacion = re.search("@", usuario) #si no está nos devuelve None
    if validacion == None:
        raise UsIncorrecto #nos manda al except con esta etiqueta
    elif  usuario != "vicente@eni.es":
        raise DiFormato
    elif contador < 1:
        raise AtaqueBloq
    
    
def intento(contador1):
    if contador1 > 0:
        try:
            usuario = input()
            errores(usuario)           
        except UsIncorrecto:
            contador1 = contador1 - 1
            print("Usuario incorrecto, introduce tu dirección de correo")
            intento(contador1)
        except DiFormato:  
            contador1 = contador1 - 1
            print("La dirección de correo tiene que tener la forma de xxx@xx.xx")
            intento(contador1)
'''  if contador1 == 1 and validacion == None:
        AtaqueBloq
        print("Por motivos de seguridad, su usuario se ha bloqueado")
        
    if validacion != None and contador1 > 0:
        try:
            usuario == "vicente@eni.es"
            print("¡Bienvenido Vicente!") 
        except DiFormato:
            contador1 = contador1 - 1
            print(contador1)
            print("La dirección de correo tiene que tener la forma de xxx@xx.xx")
            intento(contador1)
            
    if validacion == None and contador1 > 1:
        contador1 = contador1 - 1
        print(contador1)
        UsIncorrecto
        print("Usuario incorrecto, introduce tu dirección de correo")
        intento(contador1)
      
    
            
'''
contador = 3
print("Hola Vicente, por favor introduce tu correo electrónico para acceder")
intento(contador)

