entrada_distancia = input("Introduce la distancia total en metros: ")
entrada_tiempo = input("Introduce el tiempo total en segundos: ")




distancia = float(entrada_distancia)
tiempo = float(entrada_tiempo)

velocidad = distancia / tiempo 

print(f"La distancia es {distancia} m")
print(f"El tiempo total es {tiempo} s")
print(f"La velocidad es {velocidad} m/s")