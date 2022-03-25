import re

'''class Excepciones:
    def __init__(self, usuario):
        self.usuario = usuario
        
    def get_usuario(self): #método get, nos lo coge
        return self.usuario
    
    def set_usuario(self, usuario): #método set, nos servirá para modificar el sself.usuario
        self.usuario = usuario'''
    
def intento():
    usuario = input()
    if usuario == "vicente@eni.es":
        print("¡Bienvenido Vicente!")
    else:
        print("Uauario incorrecto, introduce tu dirección de correo")
        

print("Hola Vicente, por favor introduce tu correo electrónico para acceder")
intento()
#e = Excepciones(usuario)


#usuario = "t"
#usuario = "t@t.es"
#usuario = "vicente@eni.es"