entrada = input("Escribe el valor en km")
print(type(entrada))
distancia_km = float(entrada)

distancia_m = distancia_km * 1000

print(f"{entrada} km son {distancia_m} m")