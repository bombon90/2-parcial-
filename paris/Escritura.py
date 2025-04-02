# mi_script.py

CONTANTE_GLOBAL = 10 


class Escrituras():
 
        def escribe_fichero(self, mensaje):
            with open('paris.txt','a') as fichero:
                fichero.writelines(mensaje)

        def lee_fichero(self):            
            with open('paris.txt','r') as fichero:
                paris = fichero.read()
                return paris
nombre = (input(" < ingresa tu nombre > /n")) #str
edad = (input(" < ingresa la edad > /n")) #int 
comida = (input(" < ingresa tu comida favorita > /n")) # int
ciudad = (input(" < ingresa tu ciudad > /n")) # int             
paris = [nombre+'\n', edad+'\n', comida+'\n', ciudad+'\n',]       
mi_objeto = Escrituras()
mi_objeto.escribe_fichero(paris)
print(mi_objeto.lee_fichero())

