import re

'''class Excepciones:
    def __init__(self, usuario):
        self.usuario = usuario
        
    def get_usuario(self): #método get, nos lo coge
        return self.usuario
    
    def set_usuario(self, usuario): #método set, nos servirá para modificar el sself.usuario
        self.usuario = usuario'''
    
def intento(contador):
    usuario = input()
    validacion = re.search("@", usuario) #si no está nos devuelve None
    validacion2 = re.search (".", usuario)
    
    print(validacion2)
    print(validacion)
    print(contador)
    while contador < 4:
        if validacion != None:
            if usuario == "vicente@eni.es":
                print("¡Bienvenido Vicente!")
                break
            
            else:
                print("La dirección de correo tiene que tener la forma de xxx@xx.xx")
                contador = contador + 1
                intento(contador)
        elif validacion == None or validacion2 == None:
            print("Uauario incorrecto, introduce tu dirección de correo")
            contador = contador + 1
            intento(contador)
    if contador > 3:
        print("Por motivos de seguridad se le ha bloqueado")

contador = 1
print("Hola Vicente, por favor introduce tu correo electrónico para acceder")
intento(contador)
#e = Excepciones(usuario)

#usuario = "t"
#usuario = "t@t.es"
#usuario = "vicente@eni.es"