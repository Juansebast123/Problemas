puntos = [(1, 2), (2, 3), (0, 1), (3, 3)]

puntosOrdenados = sorted (puntos, key=lambda punto: punto[0]**2 + punto[1]**2)

print(puntosOrdenados)
