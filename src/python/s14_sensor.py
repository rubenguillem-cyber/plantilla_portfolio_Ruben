intensidad = int(input("Introduce el valor del bit: "))

if intensidad < 0 or intensidad >255:
    tipo = "inválido"
elif intensidad <  99: 
    tipo = "bajo"
elif intensidad < 199: 
    tipo = "medio"
else:
    tipo = "alto"


print(f"El valor del bit es {intensidad}, se trata de un valor {tipo}")