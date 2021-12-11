def decorador(func):
    def envoltura():
        print("Esto se añade a mi fn original")
        func()
    return envoltura

def saludo():
    print("Hola!")

saludo()

saludo = decorador(saludo)
saludo()

saludo = decorador(saludo)
saludo()