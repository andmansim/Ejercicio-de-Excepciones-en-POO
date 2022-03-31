import re

class UsIncorrecto(BaseException):
    def __init__(self, contador):
        
        print("Usuario incorrecto, introduce tu dirección de correo")
        self.contador = contador - 1
        print(self.contador)
        intento(self.contador)
        
''' def get_contador(self): #método get, nos lo coge
        return self.contador
    
    def set_usuario(self, usuario): #método set, nos servirá para modificar el sself.usuario
        self.usuario = usuario'''
    
def intento(contador):
    usuario = input()
    validacion = re.search("@", usuario) #si no está nos devuelve None
    print(contador)
    
    if contador == 1 and validacion == None:
        print("Por motivos de seguridad se le ha bloqueado")
        
    
    if validacion != None and contador > 0:
        if usuario == "vicente@eni.es":
            print("¡Bienvenido Vicente!")
            
        else:
            print("La dirección de correo tiene que tener la forma de xxx@xx.xx")
            contador = contador - 1
            intento(contador)
    elif validacion == None and contador > 1:
        raise UsIncorrecto(contador)
'''            print("Usuario incorrecto, introduce tu dirección de correo")
        contador = contador + 1
        intento(contador)'''
            
contador = 3
print("Hola Vicente, por favor introduce tu correo electrónico para acceder")
intento(contador)
#e = Excepciones(usuario)
