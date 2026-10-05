temperatura = float(input("Introduce el valor de la temperatura en ºC:"))

if temperatura < 10:
    print("Temperatura baja")
elif temperatura < 25:
    print("Temperatura media")
else:
    print("Temperatura alta")