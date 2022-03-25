class Excepciones:
    def __init__(self, usuario):
        self.usuario = usuario
    
    def intento(self):
        try: 
            self.usuario == "vicente@eni.es"
            print("¡Bienvenido Vicente!")
        except:
            print("Uauario incorrecto, introduce tu dirección de correo")

print("Hola Vicente, por favor introduce tu correo electrónico para acceder")

usuario = " "
e = Excepciones(usuario)
#usuario = "t"
#usuario = "t@t.es"
#usuario = "vicente@eni.es"