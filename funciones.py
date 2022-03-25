class Excepciones:
        
    def intento(self, usuario):
        try: 
            if usuario == "vicente@eni.es":
                print("¡Bienvenido Vicente!")
        except:
            print("Uauario incorrecto, introduce tu dirección de correo")

print("Hola Vicente, por favor introduce tu correo electrónico para acceder")

usuario = " "
print(usuario)
def intento(usuario1):
        try: 
            usuario1 == "vicente@eni.es"       
        except :
            print("Uauario incorrecto, introduce tu dirección de correo")
        else:
            print("¡Bienvenido Vicente!")
            

i = intento(usuario)
print(i)
#e = Excepciones()
#e.intento(usuario)

#usuario = "t"
#usuario = "t@t.es"
#usuario = "vicente@eni.es"