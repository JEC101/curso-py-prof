def make_multiplayer(x):

    def multiplayer(n):
        return x * n

    return multiplayer

times10 = make_multiplayer(10) # 10 queda como valor de x dentro de la fun multiplayer recordada
times4 = make_multiplayer(4) # 4 queda como valor de x dentro de la fn multiplayer recrodada

# en los prints, estoy pasando los valores de n para la multiplicación
print(times10(3)) 
print(times4(5))
print(times10(times4(2)))