import re

class UsIncorrecto(BaseException):
    pass
class DiFormato(BaseException):
    pass
class AtaqueBloq(BaseException):
    pass



def intento(contador1):
    if contador1 > 0:
        try:
            
            usuario = input()
            validacion = re.search("@", usuario) #si no está nos devuelve None
            if 
            print(contador1)
            print(validacion)
        except:
            print("Usuario incorrecto, introduce tu dirección de correo")
    if contador1 == 1 and validacion == None:
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
      
    
            

contador = 3
print("Hola Vicente, por favor introduce tu correo electrónico para acceder")
intento(contador)

