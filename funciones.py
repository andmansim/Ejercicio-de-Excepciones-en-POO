import re

class UsIncorrecto(BaseException):
    pass
class DiFormato(BaseException):
    pass
    
def intento(contador1):
    usuario = input()
    validacion = re.search("@", usuario) #si no está nos devuelve None
    print(contador1)
    print(validacion)
    if contador1 == 1 and validacion == None:
        print("Por motivos de seguridad, su usuario se ha bloqueado")
    
    while contador1 > 0: 
        contador1 = contador1 - 1  
        if validacion != None and contador1 > 0:
            try:
                usuario == "vicente@eni.es"
                print("¡Bienvenido Vicente!")
                break
                
            except DiFormato:
                
                print("La dirección de correo tiene que tener la forma de xxx@xx.xx")
                contador1 = contador1 - 1
                
        if validacion == None and contador1 > 1:

            raise UsIncorrecto 
            print("Usuario incorrecto, introduce tu dirección de correo")
            contador1 = contador1 - 1
            
            print(contador1)
            

contador = 3
print("Hola Vicente, por favor introduce tu correo electrónico para acceder")
intento(contador)

