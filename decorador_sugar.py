def decorador(func):
    def envoltura():
        print("Esto se añade a mi fn original")
        func()
    return envoltura

@decorador
def saludo():
    print("Hola!")

saludo()

def mayuscula(func):
    def envoltura(texto):
        return func(texto.upper())
    return envoltura

@mayuscula
def mensaje(nombre):
    print(f'{nombre}, recibiste un msj')

print(mensaje("Juan"))