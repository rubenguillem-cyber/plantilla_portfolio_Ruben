temperaturas = [18, 22, 20, 25]

contador = 0
total = 0
for temperatura in temperaturas:
    total = total + temperatura
    if temperatura > 20:
        contador = contador + 1
media = total / len(temperaturas)

print(f"Cantidad de temperaturas que superan los 20ºC: {contador}")

print(f"La suma de todas la temperaturas: {total}")

print(f"La media de las tempetaruas: {media} ºC")
